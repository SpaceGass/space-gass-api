import React from "react";
import type { ZudokuConfig } from "zudoku";
import "./styles.css";

// Build version — sourced from `info.x-space-gass-build` in the spec at
// build time so the API reference label always tracks the current SDK
// build (e.g. "Preview (build 14.50.75)") without manual updates.
import openapiSpec from "../descriptions/openapi.json";
const SPACE_GASS_BUILD: string =
  ((openapiSpec as { info?: { ["x-space-gass-build"]?: string } }).info?.[
    "x-space-gass-build"
  ]) ?? "preview";

// --- SDK code snippet helpers ---

function toPascalCase(segment: string): string {
  return segment
    .split("-")
    .map((s) => s.charAt(0).toUpperCase() + s.slice(1))
    .join("");
}

function pascalToSnake(str: string): string {
  return str
    .replace(/([A-Z])/g, (_, letter, offset) =>
      offset > 0 ? `_${letter.toLowerCase()}` : letter.toLowerCase(),
    );
}

// Kiota escapes Python reserved words with a trailing underscore
// (`/job/import/txt` → `client.job.import_.txt`, folder `import_/`).
const PY_RESERVED = new Set(["import", "from", "global", "class", "def", "in", "is", "as", "with", "for", "if", "else", "return", "pass", "lambda", "try", "except", "raise", "del", "not", "and", "or", "while", "yield", "async", "await", "assert", "break", "continue", "elif", "finally", "nonlocal", "none", "true", "false"]);
function pySegment(seg: string): string {
  const name = seg.replace(/-/g, "_").toLowerCase();
  return PY_RESERVED.has(name) ? `${name}_` : name;
}

// Classify the request body straight from the spec instead of guessing from
// the URL path. Zudoku dereferences `$ref`s but preserves the original pointer
// on a `__$ref` property (see
// node_modules/zudoku/src/lib/oas/parser/dereference/index.ts), so the exact
// component name (e.g. "MovingLoadVehicleCreate") is recoverable at runtime —
// including for list bodies (on the array's `items`) and `oneOf` members.
type BodyShape =
  | { kind: "none" }
  | { kind: "model"; type: string }
  | { kind: "modelList"; type: string }
  | { kind: "primitiveList"; csType: string; sample: string }
  | { kind: "composed"; members: string[] }
  | { kind: "multipart" }
  | { kind: "raw" };

const refName = (s: any): string | undefined => s?.__$ref?.split("/").pop();

// eslint-disable-next-line @typescript-eslint/no-explicit-any
// Which `oneOf` member a snippet shows: AS 4100 when it is one of them
// (the code the examples use), otherwise the first.
function pickComposedMember(members: string[]): string {
  return members.find((m) => /As4100/.test(m)) ?? members[0];
}

function bodyShapeFromSpec(operation: any): BodyShape {
  const content: any[] = operation?.requestBody?.content ?? [];
  if (!content.length) return { kind: "none" };
  const media = content.find((c) => c?.mediaType === "application/json");
  if (!media) {
    return content.some((c) => c?.mediaType === "multipart/form-data")
      ? { kind: "multipart" }
      : { kind: "raw" };
  }
  const schema = media.schema;
  if (refName(schema)) return { kind: "model", type: refName(schema)! };
  if (schema?.type === "array") {
    if (refName(schema.items))
      return { kind: "modelList", type: refName(schema.items)! };
    const prim: Record<string, [string, string]> = {
      integer: ["int?", "1, 2, 3"],
      number: ["double?", "1.0, 2.0"],
      string: ["string", '"a", "b"'],
    };
    const p = prim[schema.items?.type];
    if (p) return { kind: "primitiveList", csType: p[0], sample: p[1] };
    return { kind: "raw" };
  }
  // `oneOf` → one of several subclasses of a shared base type.
  const members = (schema?.oneOf ?? schema?.anyOf ?? [])
    .map(refName)
    .filter(Boolean);
  if (members.length) return { kind: "composed", members };
  return { kind: "raw" };
}

// Multipart upload endpoints have hand-maintained helpers (C#
// `Utils/UploadRequests.cs`, Python `upload_requests.py`) that take a file path.
const MULTIPART_HELPERS: Record<string, string> = {
  "job/new-from-template": "NewFromTemplateRequest",
  "job/import/txt": "ImportTxtRequest",
};

// When two sibling paths use different parameter names at the same position
// (e.g. /combination-load-cases/{id} and /combination-load-cases/{combinationCase}/items),
// Kiota merges them into one item node renamed `{<non-id name>-id}`, so the
// Python indexer becomes `by_combination_case_id`. Map collection path →
// merged Python indexer parameter name, derived from the spec.
const MERGED_PY_INDEXER_PARAMS: Record<string, string> = (() => {
  const byPrefix: Record<string, Set<string>> = {};
  for (const p of Object.keys((openapiSpec as { paths: object }).paths)) {
    const segs = p.replace(/^\//, "").split("/");
    segs.forEach((s, i) => {
      if (!s.startsWith("{")) return;
      const prefix = segs.slice(0, i).join("/");
      (byPrefix[prefix] ??= new Set()).add(s.slice(1, -1));
    });
  }
  const merged: Record<string, string> = {};
  for (const [prefix, names] of Object.entries(byPrefix)) {
    if (names.size < 2) continue;
    const named = [...names].find((n) => n !== "id");
    if (named) merged[prefix] = `${pascalToSnake(named)}_id`;
  }
  return merged;
})();

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function generateCodeSnippet({ selectedLang, operation }: any): string | false {
  if (selectedLang === "shell") return false; // fall back to default cURL generator

  const { method, path } = operation;
  const httpMethod: string = method.toUpperCase();
  const verbPascal = httpMethod.charAt(0) + httpMethod.slice(1).toLowerCase();

  // Paths are relative to the server URL (no /api/v1/ prefix)
  const cleanPath = path.replace(/^\//, "");
  const segments = cleanPath.split("/").filter(Boolean);
  const lastSegment = segments[segments.length - 1];

  const body = bodyShapeFromSpec(operation);
  const uploadHelper = MULTIPART_HELPERS[cleanPath];

  // ── C# SDK ──
  if (selectedLang === "csharp") {
    let chain = "client";
    for (const seg of segments) {
      if (seg.startsWith("{") && seg.endsWith("}")) {
        const param = seg.slice(1, -1);
        chain += `[${param}]`;
      } else {
        chain += `.${toPascalCase(seg)}`;
      }
    }

    const call = `await ${chain}.${verbPascal}Async`;
    const assign = httpMethod === "DELETE" ? "" : "var result = ";

    let code = "// C# SDK Client\n";
    switch (body.kind) {
      case "model":
        code += `var body = new ${body.type}\n`;
        code += `{\n`;
        code += `    // Set properties\n`;
        code += `};\n\n`;
        code += `${assign}${call}(body);`;
        break;
      case "modelList":
        code += `var bodies = new List<${body.type}>\n`;
        code += `{\n`;
        code += `    new ${body.type} { /* Set properties */ },\n`;
        code += `};\n\n`;
        code += `${assign}${call}(bodies);`;
        break;
      case "primitiveList":
        code += `var ids = new List<${body.csType}> { ${body.sample} };\n\n`;
        code += `${assign}${call}(ids);`;
        break;
      case "composed": {
        // The spec's `oneOf` lists subclasses of one base type; the SDK is
        // generated with the base type (tools/prepare_spec_for_kiota.py), so
        // any member is passed directly.
        const member = pickComposedMember(body.members);
        code += `// Body is one of: ${body.members.join(", ")}.\n`;
        code += `var body = new ${member}\n`;
        code += `{\n`;
        code += `    // Set properties\n`;
        code += `};\n\n`;
        code += `${assign}${call}(body);`;
        break;
      }
      case "multipart":
        if (uploadHelper) {
          code += `${assign}${call}(new ${uploadHelper}(@"C:\\path\\to\\file"));`;
        } else {
          code += `var body = new MultipartBody(); // add parts\n\n`;
          code += `${assign}${call}(body);`;
        }
        break;
      case "raw":
        code += `using Microsoft.Kiota.Abstractions.Serialization;\n\n`;
        code += `// Raw JSON body — see the request schema for its shape.\n`;
        code += `UntypedNode body = new UntypedArray(new List<UntypedNode>());\n\n`;
        code += `${assign}${call}(body);`;
        break;
      default:
        code += `${assign}${call}();`;
    }

    return code;
  }

  // ── Python SDK ──
  if (selectedLang === "python") {
    let chain = "client";
    segments.forEach((seg: string, i: number) => {
      if (seg.startsWith("{") && seg.endsWith("}")) {
        const param = seg.slice(1, -1);
        const snakeParam = pascalToSnake(param);
        const indexerParam =
          MERGED_PY_INDEXER_PARAMS[segments.slice(0, i).join("/")] ??
          snakeParam;
        chain += `.by_${indexerParam}(${snakeParam})`;
      } else {
        chain += `.${pySegment(seg)}`;
      }
    });

    const call = `await ${chain}.${httpMethod.toLowerCase()}`;
    const assign = httpMethod === "DELETE" ? "" : "result = ";

    // Models are re-exported by the `space_gass_api.models` shim; there are
    // no per-model submodules under it to import from.
    const importModels = `import space_gass_api.models as models\n\n`;

    let code = "# Python SDK Client\n";
    switch (body.kind) {
      case "model":
        code += importModels;
        code += `body = models.${body.type}(\n`;
        code += `    # Set properties\n`;
        code += `)\n\n`;
        code += `${assign}${call}(body)`;
        break;
      case "modelList":
        code += importModels;
        code += `bodies = [\n`;
        code += `    models.${body.type}(\n`;
        code += `        # Set properties\n`;
        code += `    ),\n`;
        code += `]\n\n`;
        code += `${assign}${call}(bodies)`;
        break;
      case "primitiveList":
        code += `${assign}${call}([${body.sample}])`;
        break;
      case "composed": {
        const member = pickComposedMember(body.members);
        code += importModels;
        code += `# Body is one of: ${body.members.join(", ")}.\n`;
        code += `body = models.${member}(\n`;
        code += `    # Set properties\n`;
        code += `)\n\n`;
        code += `${assign}${call}(body)`;
        break;
      }
      case "multipart":
        if (uploadHelper) {
          code += `from space_gass_api import ${uploadHelper}\n\n`;
          code += `${assign}${call}(${uploadHelper}(r"C:\\path\\to\\file"))`;
        } else {
          code += `from kiota_abstractions.multipart_body import MultipartBody\n\n`;
          code += `body = MultipartBody()  # add parts\n\n`;
          code += `${assign}${call}(body)`;
        }
        break;
      case "raw":
        code += `import json\n\n`;
        code += `# Raw JSON body — see the request schema for its shape.\n`;
        code += `body = json.dumps([]).encode()\n\n`;
        code += `${assign}${call}(body)`;
        break;
      default:
        code += `${assign}${call}()`;
    }

    return code;
  }

  return false;
}

// --- Zudoku config ---

const config: ZudokuConfig = {
  basePath: "/docs",
  slots: {
    "head-navigation-end": (
      <div style={{ display: "flex", alignItems: "center", gap: "4px" }}>
        <a
          href="https://github.com/SpaceGass/space-gass-api"
          target="_blank"
          rel="noopener noreferrer"
          title="GitHub"
          style={{ padding: "6px", display: "flex", opacity: 0.7 }}
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
        </a>
        <a
          href="https://www.spacegass.com"
          target="_blank"
          rel="noopener noreferrer"
          title="spacegass.com"
          style={{ padding: "6px", display: "flex", opacity: 0.7 }}
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path>
            <path d="M2 12h20"></path>
          </svg>
        </a>
      </div>
    ),
  },
  site: {
    title: "SpaceGass API",
    logo: {
      src: {
        light: "/logo-light.png",
        dark: "/logo-dark.png",
      },
      alt: "SpaceGass API",
      width: "200px",
    },
    banner: {
      message: (
        <div className="text-center">
          🤖 New in SPACE GASS 14.51 — the MCP server lets your AI agent
          build, analyse and design your models.{" "}
          <a href="/docs/mcp" className="font-semibold underline">
            Get started →
          </a>
        </div>
      ),
      color: "#f97316",
      dismissible: true,
    },
  },
  metadata: {
    title: "SPACE GASS API Documentation",
    description:
      "Programmatic access to SPACE GASS structural analysis data",
    favicon: "/blue-sg-256-clear-bg.ico",
  },
  theme: {
    fonts: {
      sans: "Space Grotesk",
      mono: "JetBrains Mono",
    },
    dark: {
      background: "#024f6e",
      foreground: "#f8fafc",
      card: "#035679",
      cardForeground: "#f8fafc",
      popover: "#035679",
      popoverForeground: "#f8fafc",
      primary: "#ef4444",
      primaryForeground: "#ffffff",
      secondary: "#046a94",
      secondaryForeground: "#f8fafc",
      muted: "#03567a",
      mutedForeground: "#94a3b8",
      accent: "#f97316",
      accentForeground: "#ffffff",
      destructive: "#ef4444",
      destructiveForeground: "#ffffff",
      border: "#334155",
      input: "#334155",
      ring: "#ef4444",
    },
    light: {
      background: "#f8fafc",
      foreground: "#024f6e",
      card: "#ffffff",
      cardForeground: "#035679",
      popover: "#ffffff",
      popoverForeground: "#035679",
      primary: "#ef4444",
      primaryForeground: "#ffffff",
      secondary: "#f1f5f9",
      secondaryForeground: "#024f6e",
      muted: "#f1f5f9",
      mutedForeground: "#64748b",
      accent: "#f97316",
      accentForeground: "#ffffff",
      destructive: "#ef4444",
      destructiveForeground: "#ffffff",
      border: "#cbd5e1",
      input: "#cbd5e1",
      ring: "#ef4444",
    },
  },
  syntaxHighlighting: {
    themes: {
      dark: "material-theme-ocean",
      light: "github-light",
    },
    languages: ["csharp", "python", "bash", "json", "toml"],
  },
  navigation: [
    {
      type: "category",
      label: "Documentation",
      icon: "book-open",
      items: [
        {
          type: "filter",
          placeholder: "Filter documentation",
        },
        {
          type: "doc",
          file: "overview",
          label: "Overview",
          icon: "house",
        },
        {
          type: "category",
          label: "Getting Started",
          icon: "book",
          collapsible: true,
          collapsed: false,
          items: [
            "quick-start",
            "concepts",
            "using-the-sdk",
            "authentication",
          ],
        },
        {
          type: "category",
          label: "Guides",
          icon: "compass",
          collapsible: true,
          collapsed: false,
          items: [
            "guides/service-automation",
            "guides/file-handling",
            "guides/running-analysis",
            "guides/filtering-and-querying",
            "guides/bulk-operations",
            "guides/error-handling",
          ],
        },
        {
          type: "separator",
        },
        {
          type: "doc",
          file: "licensing",
          label: "Licensing",
          icon: "key",
        },
        {
          type: "doc",
          file: "versioning",
          label: "Versioning",
          icon: "git-branch",
        },
        {
          type: "doc",
          file: "support",
          label: "Support",
          icon: "life-buoy",
        },
        {
          type: "separator",
        },
        {
          type: "link",
          label: "API Reference",
          to: "/api",
          icon: "arrow-right",
        },
      ],
    },
    {
      type: "category",
      label: "Examples",
      icon: "play",
      items: [
        {
          type: "category",
          label: "Tutorials",
          collapsible: true,
          collapsed: false,
          items: [
            "examples/simple-beam",
          ],
        },
        {
          type: "category",
          label: "Recipes",
          collapsible: true,
          collapsed: false,
          items: [
            "examples/open-your-own-file",
            "examples/save-and-close",
            "examples/run-linear-static-analysis",
            "examples/reactions-for-restrained-nodes",
            "examples/filter-results-by-case",
            "examples/switch-to-readonly",
            "examples/create-shape-builder-section",
            "examples/run-steel-design-check",
            "examples/run-steel-design",
          ],
        },
      ],
    },
    {
      // MCP tab — the SPACE GASS MCP server shipped with SPACE GASS 14.51+.
      // Pages live under pages/mcp/. The server is a local stdio exe, so only
      // desktop clients get install steps; web assistants get a "not available"
      // page. Keep client pages on the shared template (status → prerequisites
      // → steps → verify → update/remove → troubleshooting).
      type: "category",
      label: "MCP",
      icon: "bot",
      items: [
        {
          // Landing page, served at /mcp (explicit path — Zudoku warns that
          // index.mdx default paths don't resolve on static hosts).
          type: "doc",
          file: "mcp/overview",
          path: "/mcp",
          label: "Overview",
          icon: "house",
        },
        {
          type: "category",
          label: "Connect your client",
          icon: "plug",
          collapsible: true,
          collapsed: false,
          items: [
            {
              type: "doc",
              file: "mcp/claude-desktop",
              badge: { label: "Recommended", color: "green" },
            },
            "mcp/other-clients",
            "mcp/web-clients",
          ],
        },
        {
          type: "separator",
        },
        {
          type: "doc",
          file: "mcp/first-session",
          icon: "message-square",
        },
        {
          type: "doc",
          file: "mcp/tools",
          icon: "wrench",
        },
        {
          type: "doc",
          file: "mcp/troubleshooting",
          icon: "life-buoy",
        },
        {
          type: "separator",
        },
        {
          type: "link",
          label: "REST API docs",
          to: "/overview",
          icon: "arrow-right",
        },
      ],
    },
    {
      type: "link",
      label: "API Reference",
      to: "/api",
      icon: "code",
    },
  ],
  defaults: {
    apis: {
      expandAllTags: false,
      expandApiInformation: true,
    },
  },
  apis: [
    {
      type: "file",
      input: "../descriptions/openapi.json",
      path: "/api",
      label: `Preview (build ${SPACE_GASS_BUILD})`,
      options: {
        expandAllTags: false,
        expandApiInformation: true,
        showInfoPage: true,
        showVersionSelect: "always",
        disablePlayground: true,
        schemaDownload: { enabled: true },
        supportedLanguages: [
          { value: "python", label: "Python" },
          { value: "csharp", label: "C#" },
          { value: "shell", label: "cURL" },
        ],
        generateCodeSnippet,
      },
    },
    // Future versions:
    // {
    //   type: "file",
    //   input: "../descriptions/archive/openapi-v14.6.0.json",
    //   path: "/api",
    //   label: "14.6.0",
    //   options: { ... },
    // },
  ],
  // Generates sitemap.xml at build time into the deploy artifact (dist/docs/sitemap.xml,
  // served at /docs/sitemap.xml). Azure Front Door rewrites the apex /sitemap.xml to it.
  // Entries are absolute: siteUrl + basePath + page (e.g. https://api.spacegass.com/docs/quick-start).
  sitemap: {
    siteUrl: "https://api.spacegass.com",
    changefreq: "weekly",
    priority: 0.7,
  },
  search: {
    type: "pagefind",
  },
  docs: {
    files: "/pages/**/*.{md,mdx}",
    publishMarkdown: true,
    // LLM-friendly artifacts. Generated at build time alongside the site:
    //   /docs/llms.txt      — index of all pages with links (the "sitemap for LLMs")
    //   /docs/llms-full.txt — full markdown content of every page in one file
    // The API is public (no auth), so protected routes are irrelevant here.
    llms: {
      llmsTxt: true,
      llmsTxtFull: true,
      includeProtected: false,
    },
    defaultOptions: {
      suggestEdit: {
        url: "https://github.com/SpaceGass/space-gass-api/edit/main/docs/pages",
      },
    },
  },
  redirects: [{ from: "/", to: "/overview" }],
};

export default config;

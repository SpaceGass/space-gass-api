import React from "react";
import type { ZudokuConfig } from "zudoku";

// Build version — sourced from `info.x-space-gass-build` in the spec at
// build time so the API reference label always tracks the current SDK
// build (e.g. "Preview (build 14.50.75)") without manual updates.
import openapiSpec from "../descriptions/preview/openapi.json";
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

function singularize(word: string): string {
  if (word.endsWith("ies")) return word.slice(0, -3) + "y";
  if (word.endsWith("ses")) return word.slice(0, -2);
  if (word.endsWith("s")) return word.slice(0, -1);
  return word;
}

// Read the request-body model name straight from the spec instead of guessing
// it from the URL path. Zudoku dereferences `$ref`s but preserves the original
// pointer on a `__$ref` property (see
// node_modules/zudoku/src/lib/oas/parser/dereference/index.ts), so the exact
// component name (e.g. "MovingLoadVehicleCreate") is recoverable at runtime —
// including for list bodies, where the name lives on the array's `items`.
// Returns undefined for inline bodies that have no component `$ref`, in which
// case the caller falls back to the path-based heuristic below.
// eslint-disable-next-line @typescript-eslint/no-explicit-any
function bodyTypeFromSpec(operation: any): string | undefined {
  const content: any[] = operation?.requestBody?.content ?? [];
  const media =
    content.find((c) => c?.mediaType === "application/json") ?? content[0];
  const schema = media?.schema;
  // Single-object body, or array body (bulk-create / items collections).
  const ref: string | undefined = schema?.__$ref ?? schema?.items?.__$ref;
  return ref ? ref.split("/").pop() : undefined;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function generateCodeSnippet({ selectedLang, operation }: any): string | false {
  if (selectedLang === "shell") return false; // fall back to default cURL generator

  const { method, path } = operation;
  const httpMethod: string = method.toUpperCase();

  // Paths are relative to the server URL (no /api/v1/ prefix)
  const cleanPath = path.replace(/^\//, "");
  const segments = cleanPath.split("/").filter(Boolean);

  // Endpoints that take a list body rather than a single object:
  //   .../bulk      → List<{Parent}Create> (bulk-create the parent entity)
  //   .../items     → List<{Parent}Item>   (set the item collection of a parent)
  const lastSegment = segments[segments.length - 1];
  const isBulk = lastSegment === "bulk";
  const isItems = lastSegment === "items";
  const isList = isBulk || isItems;

  // Find the last non-parameter segment for deriving body type names. For
  // list endpoints, skip the literal "bulk"/"items" segment so we land on
  // the parent entity.
  const entitySegment = [...segments]
    .reverse()
    .find((s: string) => !s.startsWith("{") && s !== "bulk" && s !== "items");
  const entityName = entitySegment
    ? toPascalCase(singularize(entitySegment))
    : "Item";

  const hasBody = ["POST", "PATCH", "PUT"].includes(httpMethod);

  // Prefer the exact model name from the spec. Fall back to a path-based guess
  // only for inline request bodies that carry no component `$ref`.
  const pathGuessBodyType = isItems
    ? `${entityName}Item`
    : httpMethod === "POST"
      ? `${entityName}Create`
      : `${entityName}Update`;
  const bodyType = bodyTypeFromSpec(operation) ?? pathGuessBodyType;

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

    const asyncMethod =
      httpMethod.charAt(0) + httpMethod.slice(1).toLowerCase() + "Async";

    let code = "// C# SDK Client\n";
    if (hasBody) {
      if (isList) {
        code += `var bodies = new List<${bodyType}>\n`;
        code += `{\n`;
        code += `    new ${bodyType} { /* Set properties */ },\n`;
        code += `};\n\n`;
        code += `var result = await ${chain}.${asyncMethod}(bodies);`;
      } else {
        code += `var body = new ${bodyType}\n`;
        code += `{\n`;
        code += `    // Set properties\n`;
        code += `};\n\n`;
        code += `var result = await ${chain}.${asyncMethod}(body);`;
      }
    } else if (httpMethod === "DELETE") {
      code += `await ${chain}.${asyncMethod}();`;
    } else {
      code += `var result = await ${chain}.${asyncMethod}();`;
    }

    return code;
  }

  // ── Python SDK ──
  if (selectedLang === "python") {
    let chain = "client";
    for (const seg of segments) {
      if (seg.startsWith("{") && seg.endsWith("}")) {
        const param = seg.slice(1, -1);
        const snakeParam = pascalToSnake(param);
        chain += `.by_${snakeParam}(${snakeParam})`;
      } else {
        chain += `.${seg.replace(/-/g, "_").toLowerCase()}`;
      }
    }

    const pyMethod = httpMethod.toLowerCase();

    let code = "# Python SDK Client\n";
    if (hasBody) {
      const bodyModule = pascalToSnake(bodyType);
      code += `from space_gass_api.models.${bodyModule} import ${bodyType}\n\n`;
      if (isList) {
        code += `bodies = [\n`;
        code += `    ${bodyType}(\n`;
        code += `        # Set properties\n`;
        code += `    ),\n`;
        code += `]\n\n`;
        code += `result = await ${chain}.${pyMethod}(bodies)`;
      } else {
        code += `body = ${bodyType}(\n`;
        code += `    # Set properties\n`;
        code += `)\n\n`;
        code += `result = await ${chain}.${pyMethod}(body)`;
      }
    } else if (httpMethod === "DELETE") {
      code += `await ${chain}.${pyMethod}()`;
    } else {
      code += `result = await ${chain}.${pyMethod}()`;
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
          href="https://github.com/Spacegass/space-gass-api"
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
          🚀 Engineer the Future with the new SPACE GASS API (COMING SOON!)
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
    favicon: "/docs/blue-sg-256-clear-bg.ico",
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
    languages: ["csharp", "python", "bash", "json"],
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
          ],
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
      input: "../descriptions/preview/openapi.json",
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
        url: "https://github.com/Spacegass/space-gass-api/edit/main/docs/pages",
      },
    },
  },
  redirects: [{ from: "/", to: "/overview" }],
};

export default config;

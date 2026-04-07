import React from "react";
import type { ZudokuConfig } from "zudoku";

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

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function generateCodeSnippet({ selectedLang, operation }: any): string | false {
  if (selectedLang === "shell") return false; // fall back to default cURL generator

  const { method, path } = operation;
  const httpMethod: string = method.toUpperCase();

  // Paths are relative to the server URL (no /api/v1/ prefix)
  const cleanPath = path.replace(/^\//, "");
  const segments = cleanPath.split("/").filter(Boolean);

  // Find the last non-parameter segment for deriving body type names
  const entitySegment = [...segments]
    .reverse()
    .find((s: string) => !s.startsWith("{"));
  const entityName = entitySegment
    ? toPascalCase(singularize(entitySegment))
    : "Item";

  const hasBody = ["POST", "PATCH", "PUT"].includes(httpMethod);

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
      const bodyType =
        httpMethod === "POST" ? `${entityName}Create` : `${entityName}Update`;
      code += `var body = new ${bodyType}\n`;
      code += `{\n`;
      code += `    // Set properties\n`;
      code += `};\n\n`;
      code += `var result = await ${chain}.${asyncMethod}(body);`;
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
      const bodyType =
        httpMethod === "POST" ? `${entityName}Create` : `${entityName}Update`;
      const bodyModule = pascalToSnake(bodyType);
      code += `from spacegass_client.models.${bodyModule} import ${bodyType}\n\n`;
      code += `body = ${bodyType}(\n`;
      code += `    # Set properties\n`;
      code += `)\n\n`;
      code += `result = await ${chain}.${pyMethod}(body)`;
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
          🚀 Engineer the Future with the new SPACE GASS API
        </div>
      ),
      color: "#f97316",
      dismissible: true,
    },
  },
  metadata: {
    title: "SpaceGass API Documentation",
    description:
      "Programmatic access to SPACE GASS structural analysis data",
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
  },
  navigation: [
    {
      type: "category",
      label: "Getting Started",
      icon: "book",
      items: [
        "getting-started/introduction",
        "getting-started/quick-start",
        "getting-started/authentication",
      ],
    },
    {
      type: "category",
      label: "Guides",
      icon: "compass",
      items: [
        "guides/sdk-examples",
        "guides/file-handling",
        "guides/error-handling",
        "guides/versioning",
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
      expandApiInformation: false,
    },
  },
  apis: {
    type: "file",
    input: "../descriptions/preview/openapi.json",
    path: "/api",
    options: {
      expandAllTags: false,
      expandApiInformation: false,
      supportedLanguages: [
        { value: "python", label: "Python" },
        { value: "csharp", label: "C#" },
        { value: "shell", label: "cURL" },
      ],
      generateCodeSnippet,
    },
  },
  search: {
    type: "pagefind",
  },
  docs: {
    files: "/pages/**/*.{md,mdx}",
  },
  redirects: [{ from: "/", to: "/getting-started/introduction" }],
};

export default config;

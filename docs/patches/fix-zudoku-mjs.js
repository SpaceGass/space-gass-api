/**
 * Patches Zudoku to fix Vite 7 SSR build on Windows.
 *
 * Vite 7 outputs .mjs files for SSR builds, but Zudoku expects .js files.
 * This patch makes Zudoku accept both .js and .mjs extensions.
 *
 * See: https://github.com/zuplo/zudoku/issues (report upstream when possible)
 */
const fs = require("fs");
const path = require("path");

const loaderPath = path.join(
  __dirname,
  "..",
  "node_modules",
  "zudoku",
  "dist",
  "config",
  "loader.js",
);

const prerenderPath = path.join(
  __dirname,
  "..",
  "node_modules",
  "zudoku",
  "dist",
  "vite",
  "prerender",
  "prerender.js",
);

// Patch 1: loader.js - accept zudoku.config.mjs in addition to .js
if (fs.existsSync(loaderPath)) {
  let content = fs.readFileSync(loaderPath, "utf-8");
  const oldPattern = 'o.fileName === "zudoku.config.js"';
  const newPattern =
    '/^zudoku\\.config\\.(js|mjs)$/.test(o.fileName)';

  if (content.includes(oldPattern)) {
    content = content.replace(oldPattern, newPattern);
    fs.writeFileSync(loaderPath, content, "utf-8");
    console.log("[patch] Fixed loader.js: accept zudoku.config.mjs");
  } else {
    console.log("[patch] loader.js: already patched or pattern changed");
  }
}

// Patch 2: prerender.js - accept entry.server.mjs in addition to .js
if (fs.existsSync(prerenderPath)) {
  let content = fs.readFileSync(prerenderPath, "utf-8");

  // 2a: Add existsSync import if not already present
  const fsImportLine = 'import { readFile, rm } from "node:fs/promises";';
  const fsImportWithSync =
    'import { readFile, rm } from "node:fs/promises";\nimport { existsSync } from "node:fs";';
  if (content.includes(fsImportLine) && !content.includes('from "node:fs";')) {
    content = content.replace(fsImportLine, fsImportWithSync);
    console.log("[patch] Added existsSync import to prerender.js");
  }

  // 2b: Replace hardcoded .js path with .js/.mjs fallback
  const oldLine =
    'const entryServerPath = pathToFileURL(path.join(distDir, "server/entry.server.js")).href;';
  const newLines = [
    'const entryServerJsPath = path.join(distDir, "server/entry.server.js");',
    'const entryServerMjsPath = path.join(distDir, "server/entry.server.mjs");',
    "const entryServerFile = existsSync(entryServerJsPath) ? entryServerJsPath : entryServerMjsPath;",
    "const entryServerPath = pathToFileURL(entryServerFile).href;",
  ].join("\n    ");

  if (content.includes(oldLine)) {
    content = content.replace(oldLine, newLines);
    console.log("[patch] Fixed prerender.js: accept entry.server.mjs");
  } else {
    console.log(
      "[patch] prerender.js: already patched or pattern changed",
    );
  }

  fs.writeFileSync(prerenderPath, content, "utf-8");
}

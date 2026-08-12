/**
 * Patches Zudoku to fix the Vite SSR build on Windows.
 *
 * Vite 7+ outputs .mjs files for SSR builds, but Zudoku expects .js files.
 * This patch makes Zudoku accept both .js and .mjs extensions.
 * Still required as of zudoku 0.82.2 (Vite 8) — without it the build fails
 * with "Could not find zudoku.config entry in server build output".
 *
 * Supports both the old multi-file layout (<=0.69.x) and the new
 * single-bundle layout (>=0.70.x).
 */
const fs = require("fs");
const path = require("path");

// --- New layout (>=0.70.x): bundled into cli.js ---
const cliPath = path.join(
  __dirname,
  "..",
  "node_modules",
  "zudoku",
  "dist",
  "cli",
  "cli.js",
);

if (fs.existsSync(cliPath)) {
  let content = fs.readFileSync(cliPath, "utf-8");
  let patched = false;

  // Patch 1: Accept zudoku.config.mjs in server config lookup
  const oldConfigCheck = 'o.fileName === "zudoku.config.js"';
  const newConfigCheck = '/^zudoku\\.config\\.(js|mjs)$/.test(o.fileName)';
  if (content.includes(oldConfigCheck)) {
    content = content.replace(oldConfigCheck, newConfigCheck);
    console.log("[patch] cli.js: accept zudoku.config.mjs");
    patched = true;
  }

  // Patch 2: Accept entry.server.mjs in prerender.
  // The prerender step hardcodes `<path>.join(distDir, "server/entry.server.js")`,
  // but Vite 7+ emits `entry.server.mjs`. The minified `path` import alias drifts
  // between Zudoku releases (path21 @ 0.82.2 → path22 @ 0.82.3), so match it with
  // a regex and reuse the captured name in the existence-checked replacement.
  const entryJoinRe =
    /(\w+)\.join\(distDir,\s*"server\/entry\.server\.js"\)/;
  const entryJoinMatch = content.match(entryJoinRe);
  if (entryJoinMatch && !content.includes("entry.server.mjs")) {
    const pathVar = entryJoinMatch[1];
    const newEntryServer =
      `${pathVar}.join(distDir, existsSync(${pathVar}.join(distDir, "server/entry.server.js")) ? "server/entry.server.js" : "server/entry.server.mjs")`;
    content = content.replace(entryJoinRe, newEntryServer);
    console.log("[patch] cli.js: accept entry.server.mjs");
    patched = true;
  }

  // Patch 3: Fix external entry references in build config
  const oldExternal = '"./entry.server.js", "./zudoku.config.js"';
  const newExternal =
    '"./entry.server.js", "./entry.server.mjs", "./zudoku.config.js", "./zudoku.config.mjs"';
  if (content.includes(oldExternal)) {
    content = content.replace(oldExternal, newExternal);
    console.log("[patch] cli.js: add .mjs to external list");
    patched = true;
  }

  if (patched) {
    fs.writeFileSync(cliPath, content, "utf-8");
  } else {
    console.log("[patch] cli.js: already patched or pattern changed");
  }
}

// --- Old layout (<=0.69.x): separate files ---
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

// Patch: loader.js - accept zudoku.config.mjs
if (fs.existsSync(loaderPath)) {
  let content = fs.readFileSync(loaderPath, "utf-8");
  const oldPattern = 'o.fileName === "zudoku.config.js"';
  const newPattern = '/^zudoku\\.config\\.(js|mjs)$/.test(o.fileName)';

  if (content.includes(oldPattern)) {
    content = content.replace(oldPattern, newPattern);
    fs.writeFileSync(loaderPath, content, "utf-8");
    console.log("[patch] loader.js: accept zudoku.config.mjs");
  }
}

// Patch: prerender.js - accept entry.server.mjs
if (fs.existsSync(prerenderPath)) {
  let content = fs.readFileSync(prerenderPath, "utf-8");

  // Add existsSync import if needed
  const fsImportLine = 'import { readFile, rm } from "node:fs/promises";';
  const fsImportWithSync =
    'import { readFile, rm } from "node:fs/promises";\nimport { existsSync } from "node:fs";';
  if (content.includes(fsImportLine) && !content.includes('from "node:fs";')) {
    content = content.replace(fsImportLine, fsImportWithSync);
  }

  // Replace hardcoded .js path with fallback
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
    fs.writeFileSync(prerenderPath, content, "utf-8");
    console.log("[patch] prerender.js: accept entry.server.mjs");
  }
}

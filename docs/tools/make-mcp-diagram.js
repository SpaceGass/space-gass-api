// Generates docs/public/mcp-how-it-works-{light,dark}.svg (the illustration on
// docs/pages/mcp/overview.mdx) from one template. Run from docs/:
//   node tools/make-mcp-diagram.js public
// Palette values mirror theme.light / theme.dark in docs/zudoku.config.tsx.
const fs = require("fs");
const path = require("path");

const out = process.argv[2];
if (!out) throw new Error("usage: node make-mcp-diagram.js <docs/public dir>");

const palettes = {
  light: {
    card: "#ffffff",
    cardStroke: "#cbd5e1",
    pcFill: "#f1f5f9",
    pcStroke: "#94a3b8",
    fg: "#024f6e",
    muted: "#64748b",
    accent: "#f97316",
    icon: "#035679",
  },
  dark: {
    card: "#035679",
    cardStroke: "#3b82a0",
    pcFill: "#03567a",
    pcStroke: "#94a3b8",
    fg: "#f8fafc",
    muted: "#cbd5e1",
    accent: "#f97316",
    icon: "#f8fafc",
  },
};

const font = `font-family="'Space Grotesk', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif"`;

function card(p, x, title, subtitle, icon) {
  return `
  <g transform="translate(${x} 78)">
    <rect width="236" height="150" rx="14" fill="${p.card}" stroke="${p.cardStroke}" stroke-width="1.5"/>
    <g transform="translate(96 22)" fill="none" stroke="${p.icon}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">${icon}</g>
    <text x="118" y="104" text-anchor="middle" ${font} font-size="19" font-weight="700" fill="${p.fg}">${title}</text>
    <text x="118" y="128" text-anchor="middle" ${font} font-size="13" fill="${p.muted}">${subtitle}</text>
  </g>`;
}

// Icons are drawn in a 44x44 box.
const iconChat = `
  <path d="M6 8a4 4 0 0 1 4-4h24a4 4 0 0 1 4 4v18a4 4 0 0 1-4 4H18l-9 8v-8H10a4 4 0 0 1-4-4z"/>
  <path d="M14 14h16M14 21h10"/>`;
const iconPlug = `
  <path d="M16 4v10M28 4v10"/>
  <path d="M10 14h24v6a12 12 0 0 1-24 0z"/>
  <path d="M22 32v8"/>`;
const iconFrame = `
  <path d="M8 40V18l14-12 14 12v22"/>
  <path d="M8 26h28M8 40h28"/>
  <path d="M15 26v14M29 26v14"/>`;

function arrow(p, x) {
  // double-headed arrow between cards, centred vertically on the cards
  const y = 153;
  return `
  <g stroke="${p.accent}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M${x + 6} ${y}H${x + 28}"/>
    <path d="M${x + 11} ${y - 6}l-6 6 6 6"/>
    <path d="M${x + 23} ${y - 6}l6 6-6 6"/>
  </g>`;
}

function svg(p) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 300" width="880" height="300" role="img" aria-labelledby="t d">
  <title id="t">How the SPACE GASS MCP server fits together</title>
  <desc id="d">Inside a box labelled Your PC: your AI desktop app, the SPACE GASS MCP server, and SPACE GASS, connected by arrows. Nothing leaves your machine.</desc>
  <rect x="16" y="16" width="848" height="268" rx="20" fill="${p.pcFill}" stroke="${p.pcStroke}" stroke-width="1.5" stroke-dasharray="7 6"/>
  <g transform="translate(36 34)" fill="none" stroke="${p.muted}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <rect x="0" y="0" width="22" height="15" rx="2.5"/>
    <path d="M7 20h8M11 15v5"/>
  </g>
  <text x="66" y="47" ${font} font-size="14" font-weight="600" letter-spacing="0.08em" fill="${p.muted}">YOUR PC</text>
  ${card(p, 52, "Your AI app", "Claude Desktop, VS Code, Claude Code…", iconChat)}
  ${arrow(p, 296)}
  ${card(p, 322, "SPACE GASS MCP", "installed with SPACE GASS 14.5", iconPlug)}
  ${arrow(p, 566)}
  ${card(p, 592, "SPACE GASS", "the API service, running", iconFrame)}
  <text x="440" y="262" text-anchor="middle" ${font} font-size="14" fill="${p.muted}">Everything runs here. Your model never leaves your machine.</text>
</svg>
`;
}

for (const [name, p] of Object.entries(palettes)) {
  const file = path.join(out, `mcp-how-it-works-${name}.svg`);
  fs.writeFileSync(file, svg(p), "utf8");
  console.log("wrote", file);
}

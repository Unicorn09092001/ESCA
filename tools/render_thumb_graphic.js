// render_thumb_graphic.js — Render thumbnail_graphic.html (canvas 1280x720) ra thumbnail_graphic.jpg (JPEG 95)
// và bản 168x94 để kiểm tra độ đọc được. Theo docs/quy-tac-thumbnail-graphic.md.
// Dùng: node tools/render_thumb_graphic.js "<thư mục thumbnail của project>"
const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

(async () => {
  const dir = path.resolve(process.argv[2] || ".");
  const html = path.join(dir, "thumbnail_graphic.html");
  if (!fs.existsSync(html)) throw new Error("Không thấy " + html);
  const browser = await chromium.launch({ args: ["--allow-file-access-from-files"] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto("file://" + html);
  await page.waitForSelector("body[data-ready='1']", { timeout: 15000 });
  const layout = await page.evaluate(() => window.__layout);
  const canvas = await page.$("#c");
  const out = path.join(dir, "thumbnail_graphic.jpg");
  await canvas.screenshot({ path: out, type: "jpeg", quality: 95 });
  const small = await browser.newPage({ viewport: { width: 168, height: 94 } });
  const b64 = fs.readFileSync(out).toString("base64");
  await small.setContent(`<body style="margin:0"><img src="data:image/jpeg;base64,${b64}" width="168" height="94"></body>`);
  await small.screenshot({ path: path.join(dir, "thumbnail_graphic_168x94.jpg"), type: "jpeg", quality: 95 });
  await browser.close();
  console.log("✅", out, JSON.stringify(layout));
  if (layout.bottom > 634) console.log("⚠️  Chữ chạm dải đáy cấm (y > 634)");
})();

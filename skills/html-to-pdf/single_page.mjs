#!/usr/bin/env node
// single_page.mjs — render an HTML file to ONE content-sized PDF page.
//
// For digital, zoomable deliverables (scrolling dashboards), not print.
// Measures the rendered content height in a headless Chrome and prints a
// single page sized exactly to the content — zero internal page breaks, so
// nothing is ever sliced across a page boundary.
//
// Dependency-free: drives the already-installed Chrome over the DevTools
// Protocol using Node's built-in WebSocket + fetch (Node >= 22). No npm install.
//
// Usage: node single_page.mjs <src.html> <out.pdf> [chrome-binary]
// Exit:  0 ok · 2 bad args · 3 render failed · 5 content too tall for one page

import { spawn } from 'node:child_process';
import { mkdtempSync, readFileSync, writeFileSync, existsSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

const [, , srcArg, outArg, chromeArg] = process.argv;
if (!srcArg || !outArg) {
  console.error('usage: single_page.mjs <src.html> <out.pdf> [chrome-binary]');
  process.exit(2);
}
const CHROME = chromeArg || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const SRC = resolve(srcArg);
const OUT = resolve(outArg);
if (!existsSync(SRC)) { console.error(`ERROR: html not found: ${SRC}`); process.exit(2); }

const LAYOUT_W = 1200;          // deterministic layout width (px) — matches a desktop dashboard view
const MAX_IN = 200;             // PDF hard cap is 200in/side; bail to Letter fallback above this
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const userDir = mkdtempSync(join(tmpdir(), 'h2pdf-'));
const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--remote-debugging-port=0',
  `--user-data-dir=${userDir}`, '--no-first-run', '--no-default-browser-check',
  `--window-size=${LAYOUT_W},1000`, 'about:blank',
], { stdio: 'ignore' });

function cleanup() { try { chrome.kill(); } catch {} try { rmSync(userDir, { recursive: true, force: true }); } catch {} }

async function devtoolsPort() {
  const f = join(userDir, 'DevToolsActivePort');
  for (let i = 0; i < 600; i++) {  // ~15s — Chrome cold-starts slower when another instance is already running
    if (existsSync(f)) { const p = readFileSync(f, 'utf8').split('\n')[0].trim(); if (p) return p; }
    await sleep(25);
  }
  throw new Error('Chrome DevTools port never appeared');
}

let nextId = 0;
const pending = new Map();
const listeners = {};
function call(ws, method, params = {}) {
  const id = ++nextId;
  ws.send(JSON.stringify({ id, method, params }));
  return new Promise((res, rej) => pending.set(id, { res, rej }));
}
const onceEvent = (method) => new Promise((res) => { (listeners[method] ||= []).push(res); });

async function main() {
  const port = await devtoolsPort();
  const targets = await (await fetch(`http://127.0.0.1:${port}/json`)).json();
  const page = targets.find((t) => t.type === 'page');
  if (!page) throw new Error('no page target');

  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = () => rej(new Error('ws connect failed')); });
  ws.onmessage = (ev) => {
    const m = JSON.parse(ev.data);
    if (m.id && pending.has(m.id)) {
      const { res, rej } = pending.get(m.id); pending.delete(m.id);
      m.error ? rej(new Error(m.error.message)) : res(m.result);
    } else if (m.method && listeners[m.method]) {
      listeners[m.method].splice(0).forEach((cb) => cb(m.params));
    }
  };

  await call(ws, 'Page.enable');
  const loaded = onceEvent('Page.loadEventFired');
  await call(ws, 'Page.navigate', { url: `file://${SRC}` });
  await loaded;
  await sleep(400); // let fonts/layout settle before measuring

  const { result } = await call(ws, 'Runtime.evaluate', {
    expression: `(() => { const d = document.documentElement, b = document.body;
      return { w: Math.max(d.scrollWidth, b.scrollWidth), h: Math.max(d.scrollHeight, b.offsetHeight, d.offsetHeight) }; })()`,
    returnByValue: true,
  });
  const { w, h } = result.value;
  const paperWidth = w / 96;
  const paperHeight = (h + 2) / 96; // +2px guards a hairline second page

  if (paperHeight > MAX_IN) {
    console.error(`content is ${paperHeight.toFixed(0)}in tall — exceeds the ${MAX_IN}in single-page cap. Use the multi-page (Letter) mode instead.`);
    ws.close(); cleanup(); process.exit(5);
  }

  const pdf = await call(ws, 'Page.printToPDF', {
    printBackground: true, paperWidth, paperHeight,
    marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0,
    pageRanges: '1', // force exactly one page
  });
  writeFileSync(OUT, Buffer.from(pdf.data, 'base64'));
  console.log(`✓ single-page PDF: ${OUT}  (content ${w}×${h}px → ${paperWidth.toFixed(1)}×${paperHeight.toFixed(1)}in, 1 page)`);
  ws.close();
}

main().then(() => { cleanup(); process.exit(0); })
  .catch((e) => { console.error('ERROR:', e.message); cleanup(); process.exit(3); });

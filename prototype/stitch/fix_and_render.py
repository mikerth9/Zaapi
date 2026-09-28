"""Apply post-Stitch consistency fixes to the exported HTML and re-render PNGs.

Stitch's edit tool changes screens inside its own session but not the exported
files, so the same fixes are applied here. Originals stay in original/.

Usage: python3 fix_and_render.py [name ...]   (no names = every file in original/html)
"""
import json, pathlib, re, subprocess, sys, tempfile, time

HERE = pathlib.Path(__file__).parent
SRC, OUT = HERE / "original" / "html", HERE / "html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
WIDTH = 1440

TEXT_FIXES = [
    ("Merchant: Aisha · Rumah Kita (Kuala Lumpur)", "Rumah Kita · Kuala Lumpur"),
    ("Merchant: Pranee · Baan Samunprai (Chiang Mai)", "Baan Samunprai · Chiang Mai"),
    ("about 15 minutes left", "about 21 minutes left"),
]
# Invented claims or contradictions, removed with the element that holds them.
REMOVE_TEXT = [
    "28% completed",
    "All connections protected by 256-bit encryption",
    "Sync frequency: Real-time",
    "Target for launch: 80+",
    "Zero disruption to live human agent shifts",
    "+43%",
    "Resets at the end of your trial cycle. Unused quota does not roll over.",
    "+14% vs last week",
    "Healthy self-resolution rate",
    "Safety filters active",
]
PRIMARY_LABELS = [
    "Review topics", "Continue", "Save and re-test", "Fix this answer", "Next question",
    "Talk to us", "Go live", "Review answers", "Review all",
]

# The real app's left rail, checked in the live trial account on 28 Sep 2026 (aria-labels in
# order): store switcher, sidebar toggle | Notifications, Search | Tickets, AI Agent, Analytics,
# Automations, Broadcast, Contacts, Settings | Live Chat Support at the bottom. The seven
# sections get labels; the utility icons stay icon-only with tooltips, as they are today.
ICONS = {
    "store": '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4M10 10h4M10 14h4M10 18h4"/>',
    "sidebar": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "tickets": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/>',
    "ai": '<path d="M12 12c-2-2.67-4-4-6-4a4 4 0 1 0 0 8c2 0 4-1.33 6-4Zm0 0c2 2.67 4 4 6 4a4 4 0 0 0 0-8c-2 0-4 1.33-6 4Z"/>',
    "analytics": '<path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/>',
    "automations": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "broadcast": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "contacts": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3M12 17h.01"/>',
}


def svg(name, size=20):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


def icon_button(name, tip, badge=False):
    dot = ('<span style="position:absolute;top:7px;right:8px;width:7px;height:7px;border-radius:50%;'
           'background:#F04438;border:1.5px solid #fff"></span>') if badge else ""
    return (f'<button type="button" title="{tip}" aria-label="{tip}" style="position:relative;width:40px;height:36px;'
            f'display:flex;align-items:center;justify-content:center;border:0;background:none;border-radius:8px;'
            f'color:#667085;cursor:pointer">{svg(name)}{dot}</button>')


def section(name, label, active=False):
    colour = "#008A77" if active else "#475467"
    pill = "background:#E6F9F6;" if active else ""
    weight = 600 if active else 500
    return (f'<a title="{label}" aria-label="{label}" style="display:flex;flex-direction:column;align-items:center;gap:3px;'
            f'width:64px;padding:7px 0 6px;border-radius:8px;{pill}color:{colour};text-decoration:none;cursor:pointer">'
            f'{svg(name)}<span style="font:{weight} 11px/14px Inter,sans-serif;letter-spacing:.01em">{label}</span></a>')


DIVIDER = '<div style="width:32px;height:1px;background:#EAECF0;margin:6px 0"></div>'
NAV_HTML = (
    '<div data-zaapi-rail style="display:flex;flex-direction:column;align-items:center;gap:2px;width:72px;'
    'height:100%;min-height:100%;padding:10px 0 12px;box-sizing:border-box;background:#fff">'
    + icon_button("store", "Store: Rumah Kita")
    + icon_button("sidebar", "Show AI Agent menu (⌘B)")
    + DIVIDER
    + icon_button("bell", "Notifications", badge=True)
    + icon_button("search", "Search")
    + DIVIDER
    + section("tickets", "Tickets")
    + section("ai", "AI Agent", active=True)
    + section("analytics", "Analytics")
    + section("automations", "Automations")
    + section("broadcast", "Broadcast")
    + section("contacts", "Contacts")
    + section("settings", "Settings")
    + '<div style="flex:1"></div>'
    + icon_button("help", "Live Chat Support")
    + '</div>'
)

FIX_SCRIPT = """
<!-- Post-Stitch consistency fixes (see ../NOTES.md) -->
<script>
window.addEventListener('load', () => setTimeout(() => {
  const exact = (el, t) => el.textContent.replace(/\\s+/g, ' ').trim() === t;
  // Remove the smallest element holding each unwanted text, and any wrapper holding only that.
  const outermost = t => {
    const hits = [...document.querySelectorAll('body *')].filter(el => exact(el, t));
    return hits.filter(el => !hits.includes(el.parentElement));
  };
  // Hide the chip but keep its slot, so the centred trial banner stays centred.
  outermost('Production Preview').forEach(el => el.style.visibility = 'hidden');
  // Smallest element holding the text, widened only to a parent whose extra text is
  // an icon (a glyph or an icon-font ligature such as "trending_up"), never real copy.
  const iconOnly = r => /^[^A-Za-z0-9]*([a-z]+(_[a-z]+)*)?[^A-Za-z0-9]*$/.test(r.trim());
  const holding = t => {
    const hits = [...document.querySelectorAll('body *')].filter(el => el.textContent.includes(t));
    return hits.filter(el => ![...el.children].some(c => c.textContent.includes(t))).map(el => {
      while (el.parentElement && iconOnly(el.parentElement.textContent.replace(t, ''))) el = el.parentElement;
      return el;
    });
  };
  __REMOVE__.forEach(t => holding(t).forEach(el => el.remove()));
  // One demo control, dashed grey, never amber.
  const merchant = '__MERCHANT__';
  const header = document.querySelector('header') || document.body;
  const demo = [...header.querySelectorAll('div,span,button')].filter(el =>
      /Demo/.test(el.textContent) && el.textContent.length < 120 && /dashed/.test(el.className));
  if (demo.length) {
    demo[0].outerHTML = `<div style="display:flex;align-items:center;gap:8px;border:1px dashed #98A2B3;border-radius:6px;padding:4px 10px;background:#F9FAFB;font:500 12px Inter,sans-serif;color:#475467">
      <span style="color:#98A2B3;letter-spacing:.04em">DEMO</span><span style="color:#1D2939">${merchant} ▾</span>
      <span style="color:#D0D5DD">|</span><span>Hide notes</span><span style="color:#D0D5DD">·</span><span>Reset</span></div>`;
  }
  // Primary buttons use the AI gradient; disabled ones stay grey.
  const labels = __LABELS__;
  document.querySelectorAll('button, a').forEach(b => {
    // Drop icon-font ligatures such as "arrow_forward" before matching the label.
    const t = b.textContent.replace(/\\b[a-z]+(_[a-z]+)+\\b/g, '').replace(/\\s+/g, ' ').trim();
    if (!labels.includes(t)) return;
    if (b.disabled || /not-allowed|disabled|gray-[1-3]00|slate-[1-3]00/.test(b.className)) return;
    const cs = getComputedStyle(b);
    const filled = /gradient/.test(cs.backgroundImage) ||
      !/rgba\\(0, 0, 0, 0\\)|rgb\\(255, 255, 255\\)/.test(cs.backgroundColor);
    if (!filled) return;  // secondary (white or transparent) buttons stay as they are
    Object.assign(b.style, {background: 'linear-gradient(94deg, #1ED1BB 0%, #5E40E1 140%)', color: '#fff',
      minHeight: '40px', borderRadius: '8px', border: 'none'});
  });
  // Swap Stitch's partial left rail for the real app's full one.
  const rail = [...document.querySelectorAll('body *')].filter(el => {
    const r = el.getBoundingClientRect();
    return r.left <= 1 && r.width >= 48 && r.width <= 120 && r.height >= innerHeight * 0.6
      && /Contacts/.test(el.textContent) && /Settings/.test(el.textContent);
  }).sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height
                  - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0];
  if (rail) {
    rail.innerHTML = __NAV__;
    Object.assign(rail.style, {width: '72px', minWidth: '72px', padding: '0', overflow: 'hidden'});
  }
  // Measure full content height, including inner scroll containers.
  let h = document.documentElement.scrollHeight;
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (el.scrollHeight > el.clientHeight + 4) h = Math.max(h, r.top + el.scrollHeight);
  });
  document.documentElement.dataset.fullHeight = Math.ceil(h);
}, 1200));
</script>
"""


def nav_html(merchant):
    return NAV_HTML.replace("Store: Rumah Kita", "Store: " + merchant.split(" · ")[1])


def fix(name):
    html = (SRC / f"{name}.html").read_text()
    for a, b in TEXT_FIXES:
        html = html.replace(a, b)
    merchant = "Pranee · Baan Samunprai" if name.startswith("11_") else "Aisha · Rumah Kita"
    script = (FIX_SCRIPT.replace("__REMOVE__", json.dumps(REMOVE_TEXT))
              .replace("__LABELS__", json.dumps(PRIMARY_LABELS)).replace("__MERCHANT__", merchant).replace("__NAV__", json.dumps(nav_html(merchant))))
    html = html.replace("</body>", script + "</body>")
    out = OUT / f"{name}.html"
    out.write_text(html)
    return out


def chrome(*args, until=None):
    """Run headless Chrome. On this Mac it can finish its work and then not exit,
    so stop waiting once the output exists (a DOM dump, or the file `until`)."""
    with tempfile.TemporaryDirectory() as profile:
        proc = subprocess.Popen([CHROME, "--headless=new", "--hide-scrollbars", "--disable-gpu",
                                 f"--user-data-dir={profile}", "--virtual-time-budget=8000", *args],
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        try:
            out, _ = proc.communicate(timeout=20 if until is None else 5)
        except subprocess.TimeoutExpired:
            if until is not None:
                for _ in range(80):
                    if until.exists() and until.stat().st_size > 0:
                        time.sleep(1)
                        break
                    time.sleep(0.5)
            proc.kill()
            out, _ = proc.communicate()
        return out or ""


def render(name, path):
    dom = chrome(f"--window-size={WIDTH},900", "--dump-dom", path.as_uri())
    m = re.search(r'data-full-height="(\d+)"', dom)
    height = max(900, int(m.group(1))) if m else 900
    # Pages built on h-screen stretch to the window, so render the full height in one frame.
    png = HERE / f"{name}.png"
    png.unlink(missing_ok=True)
    chrome(f"--window-size={WIDTH},{height}", "--force-device-scale-factor=2",
           f"--screenshot={png}", path.as_uri(), until=png)
    print(f"{name}: {WIDTH}x{height}")


if __name__ == "__main__":
    names = sys.argv[1:] or sorted(p.stem for p in SRC.glob("*.html"))
    for n in names:
        render(n, fix(n))

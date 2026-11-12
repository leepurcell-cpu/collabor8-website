#!/usr/bin/env python3
"""Generates the static pages in site/. Run: python3 tools/build.py
Page copy lives in tools/pages/<name>.html (the inside of <main>). Shared header, footer and
head tags are defined here. Styles: tools/artifact.css is the source for site/assets/styles.css
(copied on build). Bump VER on every publish so browsers fetch fresh CSS and JS."""
import pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
SRC = ROOT / "tools" / "pages"
BASE = "https://collabor8.solutions"
VER = "22"
# Google Calendar booking page for the Contact page button. Empty = button box is left out.
BOOKING_URL = ""
NAV = [("Home", "/"), ("What we do", "/what-we-do/"), ("Insights", "/insights/"), ("About", "/about/"), ("Contact", "/contact/")]
LEGAL = ("Collabor8™ is a trading name of Lee Purcell for Project Management Services L.L.C. "
         "Trade Licence No. 1233040.")

# slug, source fragment, <title>, meta description, main class, page script
PAGES = [
    ("", "home", "Collabor8™ | Complex problems, solved.",
     "Management consulting from people who have run it, built it and fixed it. Any industry, any size.", "", None),
    ("what-we-do/", "what-we-do", "What we do | Collabor8™",
     "Six outcomes we help organisations reach: new markets, partnerships and deals, scale and organisation, leadership, technology and AI, and growth.", "inner", "what-we-do.js"),
    ("insights/", "insights", "Insights | Collabor8™",
     "Papers from Collabor8™: our view on the shifts reshaping markets, partnerships and technology.", "inner", None),
    ("about/", "about", "About | Collabor8™",
     "A senior team built around your problem: former corporate consultants, sector specialists and senior entrepreneurs. Paid by fees or a shared outcome.", "inner", None),
    ("contact/", "contact", "Contact | Collabor8™",
     "Contact Collabor8™. Tell us the problem, or the result you are after. A short email is enough.", "inner", None),
]


def page(slug, frag, title, desc, main_class, script, noindex=False, image="site.jpg", body=None):
    path = "/" + slug
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a></li>' for t, h in NAV
    )
    if body is None:
        body = (SRC / f"{frag}.html").read_text() if frag else ""
        if "{{BOOKING_URL}}" in body:
            import re as _r
            if BOOKING_URL:
                body = body.replace("{{BOOKING_URL}}", BOOKING_URL)
            else:
                body = _r.sub(r'\s*<div class="reach book">.*?</div>', "", body, flags=_r.S)
    cls = f' class="{main_class}"' if main_class else ""
    robots = '<meta name="robots" content="noindex, nofollow">\n' if noindex else ""
    extra = f'<script src="/assets/{script}?v={VER}" defer></script>\n' if script else ""
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Collabor8™">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{BASE}/assets/og/{image}?v={VER}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}/assets/og/{image}?v={VER}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/files/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/files/inter-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts/inter.css?v={VER}">
<link rel="stylesheet" href="/assets/styles.css?v={VER}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
  <header class="top">
    <a class="brand" href="/" aria-label="Collabor8 home"><span>Collabor8<sup>™</sup></span></a>
    <nav aria-label="Main">
      <ul>
        {nav}
      </ul>
    </nav>
  </header>

  <main id="main"{cls}>
{body}
  </main>

  <footer>
    <p class="legal">{LEGAL}</p>
  </footer>
</div>
{extra}</body>
</html>
'''
    out = SITE / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


for slug, frag, title, desc, cls, script in PAGES:
    page(slug, frag, title, desc, cls, script)

# One share page per paper (/insights/<file-name>/), so a link shared on LinkedIn or WhatsApp
# shows the paper's cover. Paper details are read from the Insights page itself.
import html as _html, re as _re
PAPER_SLUGS = []
for art in _re.findall(r'<article class="paper">(.*?)</article>', (SRC / "insights.html").read_text(), _re.S):
    pdf = _re.search(r'href="/insights/papers/([^"]+)\.pdf"', art).group(1)
    tag = _re.search(r'<p class="tag">(.*?)</p>', art, _re.S).group(1).strip()
    h3 = _re.search(r'<h3>(.*?)</h3>', art, _re.S).group(1).strip()
    hook = _re.search(r'<p class="hook">(.*?)</p>', art, _re.S).group(1).strip()
    discuss = _re.search(r'<p class="discuss">.*?</p>', art, _re.S).group(0)
    slug = f"insights/{pdf}/"
    PAPER_SLUGS.append(slug)
    body = f'''<p class="eyebrow"><a href="/insights/">Insights</a></p>
    <div class="papers single">
      <article class="paper">
        <a class="cover" href="/insights/papers/{pdf}.pdf" aria-label="Open the paper: {h3}"><img src="/insights/papers/{pdf}-cover.jpg" alt="Cover of {h3}"></a>
        <div class="pbody">
          <p class="tag">{tag}</p>
          <h1 class="ptitle">{h3}</h1>
          <p class="hook">{hook}</p>
          <a class="cta" href="/insights/papers/{pdf}.pdf">Read the paper</a>
          {discuss}
        </div>
      </article>
    </div>
    <p class="more"><a href="/insights/">More papers from Collabor8™ →</a></p>'''
    plain = _html.unescape(_re.sub("<[^>]+>", "", h3))
    page(slug, None, plain if plain.endswith("Collabor8™") else f"{plain} | Collabor8™", _html.unescape(_re.sub("<[^>]+>", "", hook)).replace('"', "&quot;"),
         "inner", None, image=f"{pdf}.jpg", body=body)

# 404 page (Netlify serves site/404.html for unknown addresses)
(SITE / "404.html").write_text(f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Collabor8™</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/fonts/inter.css?v={VER}">
<link rel="stylesheet" href="/assets/styles.css?v={VER}">
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="brand" href="/" aria-label="Collabor8 home"><span>Collabor8<sup>™</sup></span></a>
    <nav aria-label="Main"><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for t, h in NAV)}</ul></nav>
  </header>
  <main id="main" class="inner">
    <p class="eyebrow">404</p>
    <h1 class="page">That page <span class="g">is not here.</span></h1>
    <div class="rule" aria-hidden="true"></div>
    <p class="sub tight">It may have moved. Start from the home page.</p>
    <div class="cta-row"><a class="cta" href="/">Go to the home page</a></div>
  </main>
  <footer><p class="legal">{LEGAL}</p></footer>
</div>
</body>
</html>
''')

# styles
shutil.copyfile(ROOT / "tools" / "artifact.css", SITE / "assets" / "styles.css")

# robots and sitemap
(SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
(SITE / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}/{s}</loc></url>\n" for s in [p[0] for p in PAGES] + PAPER_SLUGS)
    + "</urlset>\n"
)
print("built", len(PAGES), "pages + 404")

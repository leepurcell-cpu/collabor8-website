#!/usr/bin/env python3
"""Generates the static pages in site/. Run: python3 tools/build.py
Copy follows Lee's brief exactly. Text in square brackets is a placeholder and is shown highlighted."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent / "site"
BASE = "https://zesty-daffodil-39a0bd.netlify.app"  # change to the live domain at launch
VER = "10"  # bump on every publish (cache busting)
BOOK = "mailto:lee.purcell@collabor8.solutions?subject=Book%20a%20call"
EMAIL = "lee.purcell@collabor8.solutions"
LI = "https://www.linkedin.com/in/lee-purcell-588b61b"
NAV = [("AI agents","ai-agents/"),("Contact","contact/")]  # Services, Sectors and markets, Insights, About hidden for now

def ph(s):
    """Wrap every [ ... ] in a highlighted placeholder mark."""
    return re.sub(r"\[([^\]]+)\]", r'<mark class="ph">[\1]</mark>', s)

def book(label="Book a call", note=False):
    h = f'<a class="btn" href="{BOOK}">{label}</a>'
    if note: h += '<span class="ph-note"><mark class="ph">[BOOKING LINK TO BE SUPPLIED]</mark></span>'
    return h

def page(slug, title, desc, body, desc_placeholder=False):
    depth = 0 if slug == "" else slug.count("/")
    up = "../" * depth
    url = f"{BASE}/{slug}"
    nav = "".join(f'<li><a href="{up}{h}"{" aria-current=\"page\"" if h==slug else ""}>{t}</a></li>' for t,h in NAV)
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Collabor8">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{up}fonts/files/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{up}fonts/files/inter-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{up}fonts/inter.css?v={VER}">
<link rel="stylesheet" href="{up}assets/styles.css?v={VER}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
 <div class="wrap hdr">
  <a class="logo" href="{up or './'}" aria-label="Collabor8 home">Collabor8<sup class="tm">™</sup></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main"><ul>{nav}</ul></nav>
  <a class="btn" href="{BOOK}">Book a call</a>
 </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
 <div class="wrap fgrid">
  <div>
   <p><strong>Collabor8<sup class="tm">™</sup></strong></p>
   <p>Collabor8<sup class="tm">™</sup> is a trademark and trading name of Lee Purcell for Project Management Services L.L.C, Dubai, UAE. Licence no. 1233040.</p>
   <p>Senior advice for cross-border growth.</p>
  </div>
  <div>
   <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
   <p><a href="{LI}" rel="noopener">linkedin.com/in/lee-purcell-588b61b</a></p>
   <ul class="flinks"><li><a href="{up}privacy-policy/">Privacy policy</a></li><li><a href="{up}cookie-notice/">Cookie notice</a></li></ul>
  </div>
 </div>
</footer>
<div class="cookie" id="cookie" role="region" aria-label="Cookie consent" hidden>
 <p>We use essential cookies to run this site. With your consent, we may also use analytics cookies. See our <a href="{up}cookie-notice/">Cookie notice</a>.</p>
 <div class="row"><button class="btn" type="button" data-consent-action="accepted">Accept</button><button class="btn btn-ghost" type="button" data-consent-action="declined">Decline</button></div>
</div>
<script src="{up}assets/site.js?v={VER}" defer></script>
</body>
</html>
'''
    out = ROOT / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    return slug

def sec(inner, alt=False, cls="", id=""):
    return f'<section{f' id="{id}"' if id else ""} class="{"alt " if alt else ""}{cls}"><div class="wrap">{inner}</div></section>'

home = "".join([
 sec(f'''<span class="eyebrow">Senior advice for cross-border growth.</span>
<h1>Where growth crosses borders, we advise.</h1>
<p class="lead">A senior advisory firm for large, ambitious businesses. We solve hard problems of growth and change: AI agents, GCC entry and the right partnerships.</p>
{book()}''', cls="hero"),
 '''<nav class="jump" aria-label="On this page"><div class="wrap"><span class="jump-label">On this page</span><ul><li><a href="#what-we-do">What we do</a></li><li><a href="#ai-agents">AI agents</a></li><li><a href="#who-we-advise">Who we advise</a></li><li><a href="#where-we-work">Where we work</a></li><li><a href="#how-we-work">How we work</a></li><li><a href="#selected-work">Selected work</a></li></ul></div></nav>''',
 sec('''<span class="eyebrow">What we do</span>
<div class="cols">
<div><h3>Deploy</h3><p>AI agents change how work gets done, so they need roles, rules and clear lines of approval. We design that operating model around how your business really runs, then work with specialist engineers to build, test and deploy the agents.</p><p><a href="ai-agents/">Explore AI agents</a></p></div>
<div><h3>Enter</h3><p>Businesses from outside the region face a long list of decisions. We test the market and your proposition, then set the order: onshore or free zone, licensing, core team and local partners. We manage delivery, so the first year is not spent fixing the first month.</p></div>
<div><h3>Partner</h3><p>Digital finance businesses grow fastest through networks that already hold the customers. We bring operator agreements and the right fintech partner together, and structure the commercial terms so both sides want to keep the deal.</p></div>
</div>''', alt=True, id="what-we-do"),
 sec('''<h2>AI agents, designed around your business</h2>
<p>Many AI pilots impress in a demo and stall in the business. We start with how the business actually runs: its processes, roles and rules. We design agents to fit, set who approves and who audits, and work with specialist engineers to build and deploy them. Your people stay in charge.</p>
<ol class="steps">
<li><p><strong>Map:</strong> find where agents can safely take on work.</p></li>
<li><p><strong>Design:</strong> define each agent's role, rules and approvals.</p></li>
<li><p><strong>Build:</strong> engineer and test with our technology partner.</p></li>
<li><p><strong>Govern:</strong> keep control as agents spread across the group.</p></li>
<li><p><strong>Embed:</strong> train teams so they own the result.</p></li>
</ol>''', id="ai-agents"),
 sec('''<div class="two">
<div id="who-we-advise"><span class="eyebrow">Who we advise</span><p>We advise senior decision-makers: chief executives, strategy and commercial leaders, and founders. Our deepest experience is with large multinationals, in any industry, with the GCC as our home ground. We also work with fintechs and digital finance businesses growing across Africa, and with investors who need a clear view of a deal.</p></div>
<div id="where-we-work"><span class="eyebrow">Where we work</span><p>Home ground: the GCC and wider Middle East. Regular work in Africa. Deep experience in the UK and Europe.</p></div>
</div>''', alt=True),
 sec('''<span class="eyebrow">How we work</span>
<p>Senior judgement from first call to delivery. Every engagement is led by a founder who has advised the head offices and regional hubs of large multinationals, not passed to a junior team. We recommend, then stay to see it done, and we bring the people who will run it into the plan from the start. Where the work needs engineering, we bring in specialist technology partners, so you have one plan and one accountable team.</p>''', id="how-we-work"),
 sec(f'''<span class="eyebrow">Selected work</span>
<div class="cols work">
<article><h3>Entering the Gulf</h3><p>International and large domestic businesses entered the UAE and Gulf with our support. We advised on strategy and regulatory structure, secured the required approvals and managed execution end to end.</p></article>
<article><h3>Growing across Africa</h3><p>{ph("A leading African fintech expanded across several markets through partnerships with tier-one mobile operators. We structured the deals and scaled lending products into new territories.")}</p></article>
<article><h3>Turning a business around</h3><p>{ph("A regional operation of more than 120 people was restructured around clearer segments and a sharper proposition. The plan was built with the team who had to run it. Attrition fell from over 40% to a single departure in a year.")}</p></article>
</div>''', alt=True, id="selected-work"),
 sec(f'''<h2>Tell us what you are trying to achieve.</h2>
<p>A short, confidential call is the quickest way to see whether we can help.</p>
{book()}''', cls="cta"),
])
page("", "Collabor8 | Senior advice for cross-border growth",
 "Collabor8 is a senior advisory firm helping large, ambitious businesses with AI agents, GCC market entry and partnerships. Book a call.", home)

steps = [
 ("Map","We study your processes, roles and decision points, and find where agents can take on work safely. We recommend which tasks to hand over first and which to leave with people."),
 ("Design","We define each agent's role, its rules and the point where a person approves. Designs reflect how work really flows across countries, functions and business units, not how the organisation chart says it should."),
 ("Build","Our technology partner engineers and tests the agents with your teams. Where they run is your choice. We start from your infrastructure, rules, regulation and data sovereignty needs, then deploy to fit: public cloud, a controlled setup, or fully inside your own environment."),
 ("Govern","We set who approves, who audits and how control is kept as agents spread across a group. Every action can be traced to an agent and a policy."),
 ("Embed","Agents last only if people own them. We train teams, adjust roles and involve the people who run each process from day one, so the change is theirs."),
]
ai = "".join([
 sec(f'''<span class="eyebrow">AI agents</span>
<h1>AI agents that work inside your business</h1>
<p class="lead">We design how AI agents work in complex organisations: their roles, rules and approvals. Specialist engineers build them. People stay in charge.</p>
{book()}''', cls="hero"),
 sec('''<p>Many AI pilots impress in a demo and stall in the business. The cause is rarely the technology. It is unclear roles, missing rules and teams who were not asked. We start with how the business actually runs, then design agents to fit it.</p>''', alt=True),
 sec('<span class="eyebrow">How we deploy agents</span><ol class="steps" id="steps">' + "".join(f'<li><div><h3>{t}</h3><p>{ph(d)}</p></div></li>' for t,d in steps) + '</ol>'),
 sec('''<span class="eyebrow">Strategy and technology, together</span>
<p>Most AI work fails from one side. Some firms build well but do not know the business. Some advisers know the business but cannot build. Collabor8 pairs senior business advice with deep engineering. One side judges the business, the process and the risk. The other builds and runs the technology. You get one team.</p>''', alt=True),
 sec(f'''<span class="eyebrow" id="typical-engagement">Typical engagement</span>
<p>It starts with an informal 30 minute virtual coffee, to talk through what you are trying to achieve and whether we can help. If there is a fit, we hold a working session of two to three hours to map processes and roles, shaped around your business. Then a design phase and a pilot of one or two agents in a real process. Governance is built in from the start. Scope, fees and timing are agreed in writing before work begins.</p>'''),
 sec(f'''<h2 id="agents-cta">Build a team of agents, not a single tool.</h2>
<p>We start by mapping your business: the systems, tools and subscriptions you rely on, and how each team really works. Automation brings the first quick wins. The bigger gain is agents that take on whole jobs, each with a defined role, its own skills and a knowledge base to draw on. Together they form an organisation chart of agents, used by one person or shared across hundreds. A short, confidential call is the place to start.</p>
{book()}''', alt=True, cls="cta"),
])
page("ai-agents/", "AI agents | Collabor8",
 "Collabor8 designs how AI agents work inside complex organisations: their roles, rules and approvals, built with specialist engineering partners.", ai)

# Hidden "coming soon" pages: kept in the repo, noindex, not linked from nav, footer or sitemap.
HIDDEN = [("Services","services/"),("Sectors and markets","sectors-and-markets/"),("Insights","insights/"),("About","about/")]
for t, s in HIDDEN:
    body = sec(f'''<h1>{t}</h1>
<p>Content coming soon</p>
<p class="muted">{ph(f"[PAGE TITLE TO CONFIRM: {t} | Collabor8]")}<br>{ph("[META DESCRIPTION TO BE SUPPLIED]")}</p>''', cls="hero stub")
    page(s, f"{t} | Collabor8", "[META DESCRIPTION TO BE SUPPLIED]", body)

page("contact/", "Contact | Collabor8", "Contact Collabor8. Book a short, confidential call with Lee Purcell.",
     sec(f'''<h1>Contact</h1>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p><a href="{LI}" rel="noopener">linkedin.com/in/lee-purcell-588b61b</a></p>{book()}''', cls="hero stub"))
for t, s, d in [("Privacy policy","privacy-policy/","Collabor8 privacy policy."),("Cookie notice","cookie-notice/","Collabor8 cookie notice.")]:
    page(s, f"{t} | Collabor8", d, sec(f'''<h1>{t}</h1>
<p>Content coming soon</p>''', cls="hero stub"))

urls = [""] + [h for _,h in NAV] + ["privacy-policy/","cookie-notice/"]
(ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built", len(urls), "pages")

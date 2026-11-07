# Project card: Collabor8 website

**What it is:** The Collabor8™ company website. Five pages: Home, What we do, Insights, About, Contact. Positioning: management consulting from senior people, any industry, any size; a sense check that drives contact (no figures, no client or partner names on the site pages). **Status: new site (branch `new-site`) built from the approved Claude artifact; the earlier Phase 1 AI-agents site is still live on `main` until the new site is approved.**

**Repo:** https://github.com/leepurcell-cpu/collabor8-website (private). `main` = production.

**Hosting:** Netlify, free plan. Site name `zesty-daffodil-39a0bd`, site ID `4a1bcbc8-856a-4ebd-a376-71ae754c7524`, https://zesty-daffodil-39a0bd.netlify.app. Linked to GitHub, branch `main`, publish dir `site`, no build command. Target domain: `collabor8.solutions` (with `www`), registered through Google Workspace. Email runs on this domain: do NOT move nameservers to Netlify; add website DNS records only.

**Stack:** Plain static HTML/CSS/JS in `site/`. Page copy is in `tools/pages/<name>.html` (the inside of `<main>`); `tools/build.py` adds the shared header, footer and head tags and writes `site/`. Styles: edit `tools/artifact.css` (copied to `site/assets/styles.css` on build). Tab script for What we do: `site/assets/what-we-do.js`. Inter is self-hosted (`site/fonts/`, weights 400 to 800). No CDN fonts, no cookies, no analytics, no forms.

**How to publish:**
1. Edit copy in `tools/pages/` or styles in `tools/artifact.css`, run `python3 tools/build.py`, bump `VER` in build.py.
2. Preview locally: `cd site && python3 -m http.server 8000`.
3. Commit and push. Only `main` auto-deploys; use a branch plus a draft deploy to review first.

**Rules:**
- Always write Collabor8™ with the ™. Never add "Management consultancy" after the name. No C8 tile or logo square on the website (documents and PDFs keep it).
- Footer legal line: Collabor8™ is a trading name of Lee Purcell for Project Management Services L.L.C. Trade Licence No. 1233040.
- Contact is a mailto link (lee.purcell@collabor8.solutions) plus LinkedIn. Paper links on Insights are plain PDF files in `site/insights/papers/`; each has a "Get in touch" mailto with the paper title in the subject.
- If analytics, a form or cookies are ever added, add a privacy policy and cookie notice first.

## Build log
- 2026-10-13 to 2026-10-13: earlier Phase 1 site (AI agents, chapters, colour variants) went live on `main`. Replaced by the new site once approved.
- 2026-11-07: new-site branch: five pages rebuilt from the Claude artifact, three Insights papers added, self-hosted Inter 700/800 added, domain set to collabor8.solutions in canonical and sitemap.

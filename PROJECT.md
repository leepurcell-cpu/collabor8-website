# Project card: Collabor8 website

**What it is:** The Collabor8 company website. **Status: setup only, brief to come.** Currently a "website coming soon" holding page (noindex).

**Repo:** https://github.com/leepurcell-cpu/collabor8-website (private)

**Hosting:** Netlify. Site name `SITENAME`, live at https://SITENAME.netlify.app (no custom domain, free plan).

**How to publish:**
1. Edit files in `site/` and commit to `main`.
2. Push: Netlify deploys automatically (no build command, publish dir `site`, set in netlify.toml).
3. Manual fallback: `npx netlify deploy --prod --dir site --site SITEID` (auth via NETLIFY_AUTH_TOKEN env var).
4. Check the live URL at 1440 and 390 widths, then add a build log line below.

**Quirks and gotchas:**
- Holding page carries `<meta name="robots" content="noindex, nofollow">`; remove it at launch.
- Apply Collabor8 house style (collabor8-design skill) when the real site is built; it is client facing.
- Add cache-busting to CSS/JS file names once external assets are added.

## Build log
- 2026-10-13: Repo and Netlify site set up; holding page published. https://SITENAME.netlify.app

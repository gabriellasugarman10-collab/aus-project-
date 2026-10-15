# Bound for Oz — WordPress site

Local WordPress (Docker) + a custom block theme, packaged so it can move to a new host and domain with one export and one search-replace.

Source prototype: `https://lovable.dev/preview/pwXuWiUQaiqadL7X8DbzNoHuaLRQNxUz`

## Status

| Part | State |
|---|---|
| Local stack (WP + MariaDB + WP-CLI) | ✅ |
| Block theme `theme/aus` (header, footer, 404, page, post, archive) | ✅ tested on WP 6.x/7.x, desktop + mobile |
| Pages: Home, The Pack, About (approved Lovable copy) | ✅ |
| Pack contents: Jordan's 10 sections as an accordion | ✅ |
| Book, Checkout, Free-50 pages | ⏳ placeholders — see `COPY.md` → Missing before launch |
| Design | ✅ matched to Jordan's screenshot; hex values estimated, swap for Lovable's tokens if they differ |

Copy changes and open items for Jordan: **`COPY.md`**.

## Preview in your browser (no install, no login needed)

**[Open Bound for Oz in WordPress Playground](https://playground.wordpress.net/?blueprint-url=https://raw.githubusercontent.com/gabriellasugarman10-collab/aus-project-/claude/vibe-code-wordpress-migration-r4b034/blueprint.json)**

A full WordPress runs in your browser tab, already logged in as admin (`admin` / `password`), with the theme and all pages set up from `blueprint.json`. Changes are thrown away when you close the tab, so it's for looking and trying, not saving.

## Run locally

Needs Docker Desktop.

```sh
cp .env.example .env     # set passwords
make setup               # starts stack, installs WP, activates theme, creates pages
open http://localhost:8080
```

`make down` stops it; `make reset` wipes it; `make wp ARGS="plugin list"` runs any WP-CLI command.

## Porting the Lovable design

All design decisions live in two places:

- `theme/aus/theme.json` — colours, fonts, sizes, spacing, button style. Swap the palette hex values and font stack for Lovable's Tailwind tokens (`tailwind.config.ts` / `src/index.css`).
- `theme/aus/patterns/*.php` — one file per page section set. Replace copy; add/remove sections.

Images go in via WP Admin → Media (so they migrate with `uploads/`), or `theme/aus/assets/` for theme-level graphics (logo, icons).

## Install on a live WordPress (Hostinger etc.)

1. WP Admin → Appearance → Themes → Add New → **Upload Theme** → choose `bound-for-oz-theme.zip` → Install Now.
2. Click **Activate**. Activation creates Home, The Pack, About, Book, Checkout and Free, sets Home as the front page, and switches on pretty URLs. It's safe to repeat: existing pages are never duplicated or overwritten.
3. Visit the site.

## Moving to the new host + domain

1. **Export** locally: `make export` → `backups/<timestamp>/` with `database.sql`, `uploads.tar.gz`, `aus-theme.zip`.
2. **New host**: create a fresh WordPress install (any host with SSH + WP-CLI: Kinsta, SiteGround, WP Engine, Cloudways…).
3. **Upload**: theme zip via Appearance → Themes → Upload; extract `uploads.tar.gz` into `wp-content/`.
4. **Import DB** over SSH: `wp db import database.sql`.
5. **Rewrite URLs**: `./scripts/migrate-domain.sh http://localhost:8080 https://newdomain.com` (dry-run first, then confirm).
6. **DNS**: point the domain at the host, enable SSL, then `wp option update blog_public 1` to allow indexing.

No SSH? Use the free *All-in-One WP Migration* or *Duplicator* plugin instead of steps 3–5; it does the same search-replace.

## Layout

```
docker-compose.yml   local stack
scripts/             setup · export · package-theme · migrate-domain
theme/aus/           the theme (only thing you deploy besides DB + uploads)
```

## Media

Videos live in `theme/aus/assets/video/` and ship inside the theme zip: the home page highlight film (13.6 MB) and Jordan's About page film, `about-jordan.mp4` (8.6 MB, 720p, captions burned in). Each only downloads when a visitor presses play. For anything much bigger, host it on YouTube or Vimeo and paste the link into the block instead.

Photos live in `theme/aus/assets/photos/` (hero, postcards, section images). To upgrade them, overwrite each file with a higher-res version of the same name, ideally 2400 px wide for heroes and JPEG around 80% quality.

## Changing copy

All text lives in `tools/build-patterns.py`. Edit it, run `python3 tools/build-patterns.py`, and the theme patterns regenerate. After launch, edit in WP Admin instead.

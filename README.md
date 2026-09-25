# AUS — WordPress rebuild of the Lovable prototype

Local WordPress (Docker) + a custom block theme, packaged so it can move to a new host and domain with one export and one search-replace.

Source prototype: `https://lovable.dev/preview/pwXuWiUQaiqadL7X8DbzNoHuaLRQNxUz`

## Status

| Part | State |
|---|---|
| Local stack (WP + MariaDB + WP-CLI) | ✅ |
| Block theme `theme/aus` (header, footer, 404, page, post, archive) | ✅ tested on WP 6.x/7.x, desktop + mobile |
| Pages: Home, About, Services, Contact (as editable patterns) | ✅ placeholder copy |
| Lovable design + copy ported | ⏳ blocked — prototype wasn't reachable from the build environment |
| Contact form | ⏳ add a form plugin on the final host |

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

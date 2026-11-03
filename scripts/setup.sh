#!/usr/bin/env bash
# One-shot local install: core, theme, starter pages, permalinks. Safe to re-run.
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .env ] || { cp .env.example .env; echo "Created .env from .env.example — edit passwords, then re-run."; exit 1; }
set -a; . ./.env; set +a

wp() { docker compose run --rm -T cli wp "$@"; }

echo "Waiting for WordPress…"
for _ in $(seq 1 60); do
  wp core version >/dev/null 2>&1 && wp db check >/dev/null 2>&1 && break
  sleep 2
done

if ! wp core is-installed 2>/dev/null; then
  wp core install --url="$WP_URL" --title="$WP_TITLE" \
    --admin_user="$WP_ADMIN_USER" --admin_password="$WP_ADMIN_PASSWORD" \
    --admin_email="$WP_ADMIN_EMAIL" --skip-email
  wp post delete 1 2 3 --force >/dev/null 2>&1 || true
  wp plugin delete akismet hello >/dev/null 2>&1 || true
fi

wp theme activate aus
wp rewrite structure '/%postname%/' --hard
wp option update timezone_string 'Europe/London'
wp option update blog_public 0   # keep local/staging out of search engines

page() { # slug title pattern
  local id
  id=$(wp post list --post_type=page --name="$1" --field=ID --format=ids)
  if [ -z "$id" ]; then
    id=$(wp post create --post_type=page --post_status=publish --post_name="$1" \
      --post_title="$2" --post_content="<!-- wp:pattern {\"slug\":\"aus/$3\"} /-->" \
      --meta_input='{"_wp_page_template":"page-no-title"}' --porcelain)
  fi
  echo "$id"
}

# Slugs mirror the Lovable routes so every CTA link survives the move.
home=$(page home Home home)
page pack "The Pack" pack >/dev/null
page about About about >/dev/null
page book "Book a free call" book >/dev/null
page checkout Checkout checkout >/dev/null
page free "Get the Pack free" free >/dev/null

wp option update show_on_front page
wp option update page_on_front "$home"

echo "Ready: $WP_URL  (admin: $WP_URL/wp-admin)"

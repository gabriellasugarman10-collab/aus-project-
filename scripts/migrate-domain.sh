#!/usr/bin/env bash
# Run ON THE NEW HOST (SSH + WP-CLI) after importing database.sql.
# Rewrites every URL, including serialised data, from old to new domain.
#   ./migrate-domain.sh http://localhost:8080 https://newdomain.com
set -euo pipefail
FROM="${1:?old URL, e.g. http://localhost:8080}"
TO="${2:?new URL, e.g. https://newdomain.com}"
WP="${WP_CLI:-wp}"

$WP search-replace "$FROM" "$TO" --all-tables --precise --dry-run --report-changed-only
read -rp "Apply these changes? [y/N] " ok
[ "$ok" = "y" ] || exit 1

$WP search-replace "$FROM" "$TO" --all-tables --precise --report-changed-only
$WP option update home "$TO"
$WP option update siteurl "$TO"
$WP rewrite flush --hard
$WP cache flush || true
echo "Done. When ready to go live: $WP option update blog_public 1"

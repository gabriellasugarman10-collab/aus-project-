#!/usr/bin/env bash
# Bundle everything the new host needs into backups/<timestamp>/.
set -euo pipefail
cd "$(dirname "$0")/.."
ts=$(date +%Y%m%d-%H%M%S)
out="backups/$ts"
mkdir -p "$out"

docker compose run --rm -T cli wp db export "/backups/$ts/database.sql" --add-drop-table
docker compose exec -T wordpress tar -C /var/www/html/wp-content -czf - uploads 2>/dev/null > "$out/uploads.tar.gz" || true
./scripts/package-theme.sh "$out"

echo "Export complete → $out"
ls -lh "$out"

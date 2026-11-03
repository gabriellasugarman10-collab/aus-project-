#!/usr/bin/env bash
# Zip the theme for upload via WP Admin → Appearance → Themes → Add New → Upload.
set -euo pipefail
cd "$(dirname "$0")/.."
out="${1:-backups}"
mkdir -p "$out"
(cd theme && zip -qr "../$out/aus-theme.zip" aus -x '*.DS_Store')
echo "$out/aus-theme.zip"

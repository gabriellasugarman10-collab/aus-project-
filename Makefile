.PHONY: up down setup wp export migrate zip logs reset

up:        ; docker compose up -d
down:      ; docker compose down
logs:      ; docker compose logs -f wordpress
setup: up  ; ./scripts/setup.sh
wp:        ; docker compose run --rm cli wp $(ARGS)
export:    ; ./scripts/export.sh
migrate:   ; ./scripts/migrate-domain.sh $(FROM) $(TO)
zip:       ; ./scripts/package-theme.sh
reset:     ; docker compose down -v

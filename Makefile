dk-install:
	docker compose up -d
	docker compose exec python python /code/install.py; \
	docker compose down

dk-wahapedia:
	docker compose up -d
	docker compose exec python python /code/src/wahapedia_tui.py

dk-down:
	docker compose down

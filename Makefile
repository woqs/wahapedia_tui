dk-install:
	docker compose up -d
	docker compose exec python python /code/install.py; \
	docker compose down

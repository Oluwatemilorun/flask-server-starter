PG_URI = postgresql://testuser:testpw@database
SERVER = @docker-compose exec app
DB = @docker-compose exec database

start:
	docker-compose up -d --build

build:
	docker-compose build

init-db:
	docker-compose stop app
	$(DB) bash -c "echo 'create database app' | psql $(PG_URI)"
	docker-compose start app
	$(SERVER) bash -c "source venv/bin/activate && flask db migrate -m 'Initial migration.' && flask db upgrade"

recreate-db:
	docker-compose stop app
	$(DB) bash -c "echo 'drop database app' | psql $(PG_URI) && echo 'create database app' | psql $(PG_URI)"
	docker-compose start app
	$(SERVER) bash -c "source venv/bin/activate && flask db upgrade"

start-psql:
	$(DB) psql $(PG_URI)/app

start-bash:
	$(SERVER) bash

# Run linters.
lint:
	$(SERVER) bash -c "mypy . && flake8 . && black --check --diff ."

# Format code.
format:
	$(SERVER) bash -c "black ."

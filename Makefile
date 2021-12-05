PG_URI = postgresql://testuser:testpw@database
SERVER = @docker-compose run --rm app

start:
	docker-compose up -d --build

build:
	docker-compose build

init-db:
	docker-compose stop app
	docker-compose exec database bash -c "echo 'create database app' | psql $(PG_URI)"
	docker-compose start app
	docker-compose exec app bash -c "source venv/bin/activate && flask db migrate -m 'Initial migration.' && flask db upgrade"

recreate-db:
	docker-compose stop app
	docker-compose exec database bash -c "echo 'drop database app' | psql $(PG_URI) && echo 'create database app' | psql $(PG_URI)"
	docker-compose start app
	docker-compose exec app bash -c "source venv/bin/activate && flask db upgrade"

start-psql:
	docker-compose exec database psql $(PG_URI)/app

start-bash:
	$(SERVER) bash

# Run linters.
lint:
	$(SERVER) bash -c "mypy . && flake8 . && black --check --diff ."

# Format code.
format:
	$(SERVER) bash -c "black ."

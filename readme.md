# A Simple Starter Flask App

> Built with Python + Flask + PostgreSQL + SQLAlchemy; to easily develop a solid framework for REST APIs

## Requiremnts

- Python 3.7
- Docker

## Dependencies

- [Flask 2.0.2](http://flask.pocoo.org/)
- [PostgreSQL 13](https://www.postgresql.org/)
- [SQLAlchemy 1.4](https://www.sqlalchemy.org/) for database ORM
- [Marshmallow 3.14](https://marshmallow.readthedocs.io/) for validation and serialization
- [Flask Restful 0.3](https://flask-restful.readthedocs.io/) for wrapping REST APIs
- Linting with [mypy](http://mypy-lang.org/), [flake8](http://flake8.pycqa.org/en/latest/) and [black](https://github.com/ambv/black)
- Code formatting with [black](https://github.com/ambv/black)

## Development
Docker Compose was used to avoid manually installing PostgreSQL database and to easily setup, run and develop the server and APIs

```sh
# Build and start database and server
$ make start

# Setup database and run migrations
$ make init-db

```
- Server: `http://localhost:5000`
- Database: `http://localhost:5432`
- Database Admin ([pgadmin4](https://www.pgadmin.org/docs/pgadmin4/latest/getting_started.html)): `http://localhost:5050`

### Available Scripts
- `make build`: Rebuild images / reinstall dependencies
- `make start`: Run docker compose services (database, app)
- `make init-db`: Create the initial DB and run initial migrations
- `make recreate-db`: Delete the database and re-create it
- `make start-psql`: Start PSQL cli. To exit `ctrl + d`
- `make start-bash`: Start bash in server. To exit `ctrl + d`
- `make lint`: Run linters
- `make format`: Reformat sources

### DB Migrations
DB migrations are handled by [alembic](https://alembic.sqlalchemy.org/en/latest/autogenerate.html) and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/).

`Flask-Migrate` runs migrations in the context of flask application, to use it, run `make start-bash` and then use one of the following commands:

- `flask db migrate -m "migration description"` - generate new migrations from models
- `flask db upgrade` - apply migrations to the database
- `flask db downgrade` - downgrade the database
- `flask db --help` - get help and list of available commands


## Deployment

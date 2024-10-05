# Example

## Getting started

Example is a project template to quickly start an API application.

## Development tools

- [``make``](https://cmake.org/)
- [``poetry``](https://python-poetry.org/)
- [``pre-commit``](https://pre-commit.com/)
- [``podman``](https://podman.io/)
- [``Hurl``](https://hurl.dev/)

## Local development

### Python environment

```shell
poetry env use python3.11
poetry install --with local --no-root
```

### Environment variables

The project is capable of reading ENV files that will be used to change values in Django settings.
By default, the ENV file is ``.env`` but it can be changed by setting ``DJANGO_ENV_FILE`` env variable.
[example.env](example.env) file serves as an example for such environment files.

### Django database

By default, the application uses an in-memory SQLite database that can be useful for local development or testing.
The default ``example.env`` configures a local SQLite database for more permanent changes.

### Django migrations

Once the database is properly configured, it is time to run the migrations.

```shell
python manage.py migrate
```

### Application superuser

The example env file also provides values for several variables needed to create the superuser without any interaction.
Those are:

- ``DJANGO_SUPERUSER_PASSWORD``
- ``DJANGO_SUPERUSER_USERNAME``
- ``DJANGO_SUPERUSER_EMAIL``

This project also provides a make shortcut for that.

```shell
make super-user
```

### Django commands

Once the database and the environment variables are configured, all Django commands can be executed locally without the need of any extra service or virtual machine.

```shell
python manage.py runserver
```

## QA & Testing

To emulate CI pipelines locally by means of a ``make`` target.

```shell
make ci
```

## Authors and acknowledgment
Feel free to add yourself to this list if you make a considerable contribution.

- Yunier Rojas García

## License
MIT


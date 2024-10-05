FROM bitnami/python:3.11
LABEL maintainer="pepe@cojo.es"

# Configure Python
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Configure Poetry
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache

RUN apt-get clean && apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/*

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="/opt/.cache/virtualenvs/example-9TtSrW0h-py3.11/bin:${PATH}:${POETRY_VENV}/bin"

RUN groupadd -g 10001 worker && \
   useradd -u 10000 -g worker worker \
   && chown -R worker:worker /app \
   && chown -R worker:worker /opt

USER worker:worker

WORKDIR /app

# Install dependencies
COPY --chown=worker:worker poetry.lock pyproject.toml ./


RUN poetry install --only main --no-root --no-interaction --no-ansi
RUN poetry env info --path
RUN poetry env info --path && [ "$(poetry env info --path)" = "/opt/.cache/virtualenvs/example-9TtSrW0h-py3.11" ]

# copy code
COPY --chown=worker:worker example /app/example
COPY --chown=worker:worker ./manage.py /app/


EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "example.wsgi"]

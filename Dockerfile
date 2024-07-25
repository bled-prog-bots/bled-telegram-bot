# "Build" image
FROM python:3.12.4-alpine3.20 as builder

# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# "Poetry install" image
FROM builder as poetry-installation

RUN python -m venv $POETRY_VENV \
      && $POETRY_VENV/bin/pip install -U pip setuptools \
	  && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}


# "Run" image
FROM builder as app

COPY --from=poetry-installation ${POETRY_VENV} ${POETRY_VENV}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app
COPY poetry.lock pyproject.toml ./

# Install Dependencies
RUN poetry install --no-interaction --no-cache --no-dev

COPY . /app
CMD ["poetry", "run",  "python", "main.py"]
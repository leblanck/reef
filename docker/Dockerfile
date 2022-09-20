# syntax=docker/dockerfile:experimental

# --- Release with Slim ----
FROM python:3.10.4-bullseye AS release

LABEL maintainer="Kyle LeBlanc"
LABEL tag="reef image"

# Install depdendencies
WORKDIR /app
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --without dev

COPY . /app

# Default CMD for Reef
CMD ["python", "-m", "reef.bot""]
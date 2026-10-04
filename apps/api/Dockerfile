FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
RUN pip install poetry==1.8.3
WORKDIR /app
COPY apps/api/pyproject.toml ./pyproject.toml
RUN poetry install --no-root
COPY apps/api/src ./src
COPY apps/api/alembic.ini ./alembic.ini
COPY apps/api/migrations ./migrations
COPY tests ./tests
RUN useradd -m app && chown -R app:app /app
USER app
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

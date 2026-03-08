FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:0.6.6 /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --python /usr/local/bin/python3

RUN .venv/bin/playwright install --with-deps chromium

COPY . .

ENV PYTHONPATH=/app

CMD [".venv/bin/pytest", "./tests/"]
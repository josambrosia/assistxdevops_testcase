# ================================
# 1) BUILDER STAGE
# ================================
FROM python:3.12-alpine AS builder


RUN apk add --no-cache gcc musl-dev

WORKDIR /app

COPY . /app

RUN python -m venv /venv \
    && /venv/bin/pip install --no-cache-dir fastapi uvicorn

# ================================
# 2) RUNTIME STAGE
# ================================
FROM python:3.12-alpine

RUN apk add --no-cache libstdc++ libgcc

COPY --from=builder /venv /venv
COPY --from=builder /app /app

WORKDIR /app

RUN adduser -D appuser
USER appuser

EXPOSE 8080

CMD ["/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
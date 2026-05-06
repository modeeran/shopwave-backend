# ShopWave Backend

Python/FastAPI REST API for the ShopWave e-commerce platform.

## Tech Stack
- Python 3.12 + FastAPI 0.115
- PostgreSQL 16 + SQLAlchemy (async) + Alembic
- Redis 7 (sessions, cache, queues)
- Stripe Payments + Firebase (push)
- AWS ECS Fargate + RDS + ElastiCache

## Quick Start
```bash
cp .env.example .env
docker compose up -d        # postgres + redis
uv sync
uv run uvicorn src.main:app --reload
```

## Project Structure
```
src/
  api/          # Route handlers
  models/       # SQLAlchemy ORM models
  schemas/      # Pydantic request/response models
  services/     # Business logic
  core/         # Config, security, database session
  migrations/   # Alembic migration scripts
```

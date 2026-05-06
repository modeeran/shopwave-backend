from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://shopwave:password@localhost:5432/shopwave"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30
    stripe_secret_key: str = ""
    firebase_credentials_json: str = "{}"

    class Config:
        env_file = ".env"

settings = Settings()

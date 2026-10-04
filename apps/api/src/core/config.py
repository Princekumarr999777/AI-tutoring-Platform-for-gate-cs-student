from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://gate:gate@db:5432/gate"
    redis_url: str = "redis://redis:6379/0"
    jwt_secret_key: str = "development-only-change-me"
    jwt_algorithm: str = "HS256"
    access_token_minutes: int = 30
    refresh_token_days: int = 7
    web_origin: str = "http://localhost:3000"
    class Config:
        env_file = ".env"
settings = Settings()

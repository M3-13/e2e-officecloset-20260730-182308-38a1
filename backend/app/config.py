from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str = Field(..., description="JWT signing secret (required, set via env)")
    DATABASE_URL: str = Field(..., description="Database URL (required, set via env)")
    CORS_ORIGIN: str = "http://localhost:5173"
    UPLOAD_DIR: str = "uploaded_images"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


@lru_cache
def _get_settings() -> Settings:
    return Settings()


def __getattr__(name: str) -> object:
    if name == "settings":
        return _get_settings()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

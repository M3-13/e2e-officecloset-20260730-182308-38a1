from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str = ""
    DATABASE_URL: str = "sqlite:///./wardrobe.db"
    CORS_ORIGIN: str = "http://localhost:5173"
    UPLOAD_DIR: str = "uploaded_images"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


settings = Settings()

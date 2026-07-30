import os


def pytest_configure() -> None:
    os.environ.setdefault("JWT_SECRET", "test-jwt-secret-for-pytest")
    os.environ.setdefault("DATABASE_URL", "sqlite:///./test-wardrobe.db")

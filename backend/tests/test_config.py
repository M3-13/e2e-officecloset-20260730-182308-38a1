"""Tests for config module."""

import pytest
from pydantic import ValidationError

from app.config import Settings


def test_settings_defaults() -> None:
    s = Settings(JWT_SECRET="test-secret", DATABASE_URL="sqlite:///./wardrobe.db")
    assert s.DATABASE_URL == "sqlite:///./wardrobe.db"
    assert s.CORS_ORIGIN == "http://localhost:5173"
    assert s.UPLOAD_DIR == "uploaded_images"
    assert s.JWT_SECRET == "test-secret"


def test_jwt_secret_required(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.delenv("JWT_SECRET", raising=False)
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")
    with pytest.raises(ValidationError):
        Settings()


def test_database_url_required(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("JWT_SECRET", "test-secret")
    with pytest.raises(ValidationError):
        Settings()


def test_settings_from_env(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")
    monkeypatch.setenv("JWT_SECRET", "super-secret")
    monkeypatch.setenv("CORS_ORIGIN", "http://example.com")
    monkeypatch.setenv("UPLOAD_DIR", "test_uploads")
    s = Settings()
    assert s.DATABASE_URL == "sqlite:///./test.db"
    assert s.JWT_SECRET == "super-secret"
    assert s.CORS_ORIGIN == "http://example.com"
    assert s.UPLOAD_DIR == "test_uploads"

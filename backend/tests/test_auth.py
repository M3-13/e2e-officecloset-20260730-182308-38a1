"""Tests for auth stubs."""

import pytest
from fastapi import HTTPException

from app.auth import create_access_token, get_current_user, hash_password, verify_password


def test_get_current_user_raises_501() -> None:
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(None, None)  # type: ignore[arg-type]
    assert exc_info.value.status_code == 501


def test_create_access_token_raises() -> None:
    with pytest.raises(NotImplementedError):
        create_access_token({"sub": "1"})


def test_verify_password_raises() -> None:
    with pytest.raises(NotImplementedError):
        verify_password("plain", "hashed")


def test_hash_password_raises() -> None:
    with pytest.raises(NotImplementedError):
        hash_password("plain")

"""Tests for Pydantic schemas."""

import pytest
from pydantic import ValidationError

from app.models import ClothingCategory
from app.schemas import (
    ClothingItemCreate,
    ClothingItemResponse,
    ClothingItemUpdate,
    TokenResponse,
    UserCreate,
    UserResponse,
)


def test_user_create_valid() -> None:
    u = UserCreate(email="test@example.com", password="Password1")
    assert u.email == "test@example.com"
    assert u.password == "Password1"


def test_user_create_invalid_email() -> None:
    with pytest.raises(ValidationError):
        UserCreate(email="not-an-email", password="Password1")


def test_user_create_short_password() -> None:
    with pytest.raises(ValidationError):
        UserCreate(email="test@example.com", password="Ab1")  # < 8 chars


def test_user_response_shape() -> None:
    assert set(UserResponse.model_fields.keys()) == {"id", "email", "created_at"}


def test_token_response_shape() -> None:
    t = TokenResponse(access_token="abc123")
    assert t.access_token == "abc123"
    assert t.token_type == "bearer"


def test_clothing_item_create_valid() -> None:
    c = ClothingItemCreate(name="Red Dress", category=ClothingCategory.DRESSES)
    assert c.name == "Red Dress"
    assert c.category == ClothingCategory.DRESSES


def test_clothing_item_create_empty_name() -> None:
    with pytest.raises(ValidationError):
        ClothingItemCreate(name="", category=ClothingCategory.TOPS)


def test_clothing_item_update_partial() -> None:
    c = ClothingItemUpdate(name="Updated Name")
    assert c.name == "Updated Name"
    assert c.category is None
    assert c.image_filename is None


def test_clothing_item_response_shape() -> None:
    assert set(ClothingItemResponse.model_fields.keys()) == {
        "id",
        "user_id",
        "name",
        "category",
        "image_filename",
        "created_at",
        "updated_at",
    }

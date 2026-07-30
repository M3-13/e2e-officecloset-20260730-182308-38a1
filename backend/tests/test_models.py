"""Tests for data models."""

from app.models import ClothingCategory, ClothingItem, User


def test_clothing_category_enum() -> None:
    assert ClothingCategory.TOPS.value == "tops"
    assert ClothingCategory.BOTTOMS.value == "bottoms"
    assert ClothingCategory.DRESSES.value == "dresses"
    assert ClothingCategory.OUTERWEAR.value == "outerwear"
    assert ClothingCategory.SHOES.value == "shoes"
    assert ClothingCategory.ACCESSORIES.value == "accessories"


def test_user_model_fields() -> None:
    assert hasattr(User, "id")
    assert hasattr(User, "email")
    assert hasattr(User, "hashed_password")
    assert hasattr(User, "created_at")
    assert hasattr(User, "clothing_items")


def test_clothing_item_model_fields() -> None:
    assert hasattr(ClothingItem, "id")
    assert hasattr(ClothingItem, "user_id")
    assert hasattr(ClothingItem, "name")
    assert hasattr(ClothingItem, "category")
    assert hasattr(ClothingItem, "image_filename")
    assert hasattr(ClothingItem, "created_at")
    assert hasattr(ClothingItem, "updated_at")
    assert hasattr(ClothingItem, "owner")


def test_user_table_name() -> None:
    assert User.__tablename__ == "users"


def test_clothing_item_table_name() -> None:
    assert ClothingItem.__tablename__ == "clothing_items"

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.models import ClothingCategory


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class ClothingItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    category: ClothingCategory


class ClothingItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    category: ClothingCategory | None = None
    image_filename: str | None = None


class ClothingItemResponse(BaseModel):
    id: int
    user_id: int
    name: str
    category: ClothingCategory
    image_filename: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

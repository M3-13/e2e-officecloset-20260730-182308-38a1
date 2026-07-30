from fastapi import HTTPException, Request
from sqlalchemy.orm import Session


def get_current_user(request: Request, db: Session) -> None:
    raise HTTPException(status_code=501, detail="Not implemented")


def create_access_token(data: dict) -> str:
    raise NotImplementedError


def verify_password(plain: str, hashed: str) -> bool:
    raise NotImplementedError


def hash_password(plain: str) -> str:
    raise NotImplementedError

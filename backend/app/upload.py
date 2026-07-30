from fastapi import UploadFile


def save_image(file: UploadFile) -> str:
    raise NotImplementedError


def strip_exif(path: str) -> None:
    raise NotImplementedError


def validate_image(file: UploadFile) -> None:
    raise NotImplementedError

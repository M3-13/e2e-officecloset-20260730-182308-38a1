"""Tests for upload stubs."""

import pytest

from app.upload import save_image, strip_exif, validate_image


def test_save_image_raises() -> None:
    with pytest.raises(NotImplementedError):
        save_image(None)  # type: ignore[arg-type]


def test_strip_exif_raises() -> None:
    with pytest.raises(NotImplementedError):
        strip_exif("/fake/path.jpg")


def test_validate_image_raises() -> None:
    with pytest.raises(NotImplementedError):
        validate_image(None)  # type: ignore[arg-type]

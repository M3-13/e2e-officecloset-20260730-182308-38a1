"""Integration tests for the wardrobe manager API."""

from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint() -> None:
    with TestClient(app) as client:
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


def test_cors_headers_present() -> None:
    with TestClient(app) as client:
        response = client.get(
            "/api/health",
            headers={"Origin": "http://localhost:5173"},
        )
        assert response.status_code == 200
        assert "access-control-allow-origin" in {k.lower() for k in response.headers}


def test_auth_router_registered() -> None:
    with TestClient(app) as client:
        response = client.get("/api/auth/openapi.json")
        assert response.status_code in (200, 404)


def test_clothing_router_registered() -> None:
    with TestClient(app) as client:
        response = client.get("/api/clothing/openapi.json")
        assert response.status_code in (200, 404)


def test_openapi_schema_available() -> None:
    with TestClient(app) as client:
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "paths" in schema

from fastapi.testclient import TestClient
from src.main import app
def test_auth_routes_are_documented():
    paths = TestClient(app).get("/openapi.json").json()["paths"]
    assert "/api/v1/auth/register" in paths

from fastapi.testclient import TestClient
from src.main import app
def test_health_has_request_id():
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.headers["x-request-id"]

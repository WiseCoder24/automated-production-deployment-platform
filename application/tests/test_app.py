import app


def test_home_endpoint():
    response = app.app.test_client().get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "DevOps Status App"
    assert data["status"] == "running"


def test_health_endpoint():
    response = app.app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_version_endpoint():
    response = app.app.test_client().get("/version")

    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "DevOps Status App"
    assert data["version"] == "1.0.0"
import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_API(client):
    response = client.get("/")
    assert b"Welcome to Customer Management System" in response.data

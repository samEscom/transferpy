import pytest
from app import app


# Crea un cliente de prueba
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

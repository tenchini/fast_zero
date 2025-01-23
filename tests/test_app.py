from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organizar)

    response = client.get("/")  # Act (agir)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.json() == {"message": "Olá mundo!"}  # Assert (afirmar)

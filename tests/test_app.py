from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # Act (agir)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.json() == {"message": "Olá Mundo!"}  # Assert (afirmar)


def test_create_user(client):
    response = client.post(  # UserSchema
        "/users/",
        json={
            "username": "testusername",
            "email": "test@test.com",
            "password": "password",
        },
    )

    # VOltou status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        "username": "testusername",
        "email": "test@test.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        "users": [
            {
                "username": "testusername",
                "email": "test@test.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "testusername2",
            "email": "test2@test.com",
            "password": "password",
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        "id": 1,
        "username": "testusername2",
        "email": "test2@test.com",
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {"message": "User deleted"}


def test_update_user_should_return_not_found(client):
    response = client.put(
        "/users/666",
        json={
            "username": "testusername2",
            "email": "test2@test.com",
            "password": "password",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {"detail": "User not found"}


def test_delete_should_return_not_found(client):
    response = client.delete("/users/666")

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {"detail": "User not found"}

    # def test_read_user_should_return_user_id(client):
    # response = client.get("/users/1")

    # assert response.status_code == HTTPStatus.OK

    # assert response.json() == {
    #     "username": "bob",
    #     "email": "bob@test.com",
    #     "id": 1,
    # }


def test_read_user_should_return_not_found(client):
    response = client.get("/users/666")

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {"detail": "User not found"}

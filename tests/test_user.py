import requests


def test_users_endpoint_returns_200(mocker):
    # Mock the requests.get call
    mock_get = mocker.patch("requests.get")

    # Configure the mock response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mock_get.return_value = mock_response

    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "qwerty"}

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text == ""


def test_users_endpoint_returns_401_with_wrong_password(mocker):
    # Mock the requests.get call
    mock_get = mocker.patch("requests.get")

    # Configure the mock response
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mock_get.return_value = mock_response

    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "admin"}

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text == ""

from example.config import Config


def test_home(client):
    response = client.get(f"{Config.APPLICATION_ROOT}/")
    print(response.text)
    assert response.status_code == 200

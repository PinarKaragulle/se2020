from se2020.server import app


def test_root_endpoint_should_return_hello_message():
    client = app.test_client()
    response = client.get("/")
    assert response.json == {"result": "Hello, world"}


def test_morse_endpoint_should_return_threedotsthreedashes_for_sos():
    client = app.test_client()
    response = client.get("/morse/sos")
    assert response.json == {"result": "... --- ... "}

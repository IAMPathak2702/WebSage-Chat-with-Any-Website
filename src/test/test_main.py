import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Functional Testing
def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "URL" in response.text

def test_valid_url_submission():
    url = "https://iampathak2702.github.io/Resume/"
    response = client.post("/", data={"url": url})
    assert response.status_code == 200  # Assuming the / route returns 200 for a successful submission
    assert "Invalid URL format" not in response.text  # Check that the error message is not present

def test_invalid_url_submission():
    url = "invalidurl"
    response = client.post("/", data={"url": url})
    assert response.status_code == 200
    assert "Invalid URL format" in response.text

def test_chat_page():
    response = client.get("/index")
    assert response.status_code == 200
    assert "Chat" in response.text

def test_websocket_chat():
    # This test requires a separate client for WebSocket communication
    with client.websocket_connect("/ws") as websocket:
        user_input = "Hello"
        websocket.send_text(user_input)
        response = websocket.receive_text()
        assert response.startswith(user_input)

# Performance Testing
@pytest.mark.parametrize("num_requests", [10, 100, 1000])
def test_response_time(num_requests):
    url = "https://iampathak2702.github.io/Resume/"
    client.post("/", data={"url": url})

    for _ in range(num_requests):
        response = client.get("/index")
        assert response.status_code == 200


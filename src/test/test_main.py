import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the parent directory of the current file to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module from the parent directory
from src.main import app


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

# Performance Testing
@pytest.mark.parametrize("num_requests", [10, 100, 1000])
def test_response_time(num_requests):
    url = "https://iampathak2702.github.io/Resume/"
    client.post("/", data={"url": url})

    for _ in range(num_requests):
        response = client.get("/index")
        assert response.status_code == 200


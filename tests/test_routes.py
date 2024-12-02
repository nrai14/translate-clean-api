import pytest
from translate import app # Flask app imported here


# Pytest fixture to create a test client for testing the API
@pytest.fixture
def client():
    app.testing = True  # Puts the app into testing mode
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route."""
    response = client.get('/')  # Call the index route
    assert response.status_code == 200  # Check if the response is OK
    assert b"Welcome to Nish's Translation API. Where you provide the text, and we'll translate the rest!" in response.data  # Check if the welcome message is in the response

def test_translate_invalid_payload(client):
    """Test the /translate route with invalid data."""
    response = client.post('/translate', json={})  # Send an empty payload
    assert response.status_code == 400  # Expect a 400 Bad Request
    assert b"Invalid request data" in response.data  # Check if the error message is returned

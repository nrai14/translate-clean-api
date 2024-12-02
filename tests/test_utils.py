from app.utils import cleanse_words, validate_request_data  # Import helper functions

def test_cleanse_words():
    """Test the cleansing of words."""
    words = ["Hello!", "Wrold??", "123test"]
    cleaned_words = cleanse_words(words)  # Call the function
    assert cleaned_words == ["hello", "world", "test"]  # Expected output

def test_validate_request_data():
    """Test if the request data is validated correctly."""
    valid_data = {"words": ["hello", "world"], "targetLanguage": "es"}
    invalid_data = {"words": "not a list", "targetLanguage": "es"}
    
    assert validate_request_data(valid_data) is True  # Should pass validation
    assert validate_request_data(invalid_data) is False  # Should fail validation

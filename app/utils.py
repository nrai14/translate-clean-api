# app/utils.py

import re
from spellchecker import SpellChecker
import time
import logging

# Instantiate SpellChecker globally
spell = SpellChecker()

# Cleanse and spell-check words
def cleanse_words(words):
    # Start timing for this function
    start_time = time.perf_counter()
    
    # Remove special characters, convert to lowercase, and correct misspelled words in a batch
    cleaned_words = [re.sub(r"[^a-z\s]", "", word.lower()) for word in words]
    misspelled = spell.unknown(cleaned_words)
    corrected_words = [spell.correction(word) if word in misspelled else word for word in cleaned_words]

    # Log the timing
    logging.info(f"Cleaned and spell-checked {len(words)} words in {time.perf_counter() - start_time:.2f} seconds.")
    return corrected_words

# Validate the request payload
def validate_request_data(data):
    required_keys = ('words', 'targetLanguage')
    return data and all(key in data and isinstance(data[key], list if key == "words" else str) for key in required_keys)
from app import app
from flask import jsonify, request
import requests
import logging
import re
from spellchecker import SpellChecker


# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to Nish's Translation API. Where you provide the text, and we'll translate the rest"

def cleanse_word(word):
    spell = SpellChecker()
    # Step 1: Remove special characters and convert to lowercase
    cleaned_word = re.sub(r"[^a-z\s]", "", word.lower())
    # Step 2: Check if the word is misspelled
    misspelled = spell.unknown([cleaned_word])  # SpellChecker expects a list
    # Step 3: Correct the word if it's misspelled
    if misspelled:
        corrected_word = spell.correction(cleaned_word)  # Get the most probable correction
        logging.info(f"Word '{word}' corrected to '{corrected_word}'")
        return corrected_word
    return cleaned_word

def validate_request_data(data):
    required_keys = ('words', 'targetLanguage')
    return data and all(key in data and isinstance(data[key], list if key == "words" else str) for key in required_keys)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        localURL = "http://localhost:5002/translate"  # LibreTranslate Docker URL

        # Parse and validate incoming JSON request data
        data = request.get_json()
        logging.info(f"Received request data: {data}")

        if not validate_request_data(data):
            return jsonify({"error": "Invalid request data"}), 400

        words = list(set(data["words"]))  # Deduplicate words
        target_language = data["targetLanguage"]

        translated_words = []

        for word in words:
            clean_word = cleanse_word(word)
            payload = {"q": clean_word, "source": "en", "target": target_language}
            logging.info(f"Translating word '{word}' with payload: {payload}")

            # Make the request to LibreTranslate
            response = requests.post(localURL, json=payload, headers={"Content-Type": "application/json"})
            if response.status_code == 200:
                translated_text = response.json().get("translatedText", "")
                translated_words.append({"originalWord": word, "translatedWord": translated_text})
            else:
                logging.error(f"Error translating word '{word}': {response.text}")
                return jsonify({"error": "Translation failed", "details": response.text}), 500

        # Prepare and return the response
        response_data = {"words": translated_words, "targetLanguage": target_language}
        logging.info(f"Translation response: {response_data}")
        return jsonify(response_data), 200

    except Exception as e:
        logging.critical(f"Unexpected server error: {str(e)}")
        return jsonify({"error": "Unexpected server error", "details": str(e)}), 500

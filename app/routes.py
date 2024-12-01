from app import app
from flask import jsonify, request
import requests
import logging
import re
from spellchecker import SpellChecker
import time
from app.utils import cleanse_words, validate_request_data


# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Instantiate SpellChecker globally to avoid repeated initialisation
spell = SpellChecker()

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to Nish's Translation API. Where you provide the text, and we'll translate the rest!"



@app.route('/translate', methods=['POST'])
def translate():
    try:
        localURL = "http://localhost:5002/translate"  # LibreTranslate Docker URL

        # Parse and validate incoming JSON request data
        data = request.get_json()
        logging.info(f"Received request data: {data}")

        if not validate_request_data(data):
            return jsonify({"error": "Invalid request data"}), 400

        
        target_language = data["targetLanguage"]

        # Start timing for cleansing words
        start_time_cleaning = time.perf_counter()

        # Cleanse words in a batch
        clean_words = cleanse_words(data["words"])

        # Changed deduplicate to occur AFTER cleansing 
        logging.info(f"Words before deduplication: {clean_words}")
        deduplicated_words = list(set(clean_words))
        logging.info(f"Words after deduplication: {deduplicated_words}")


        logging.info(f"Total time for cleansing words: {time.perf_counter() - start_time_cleaning:.2f} seconds.")

        # Start timing for batch translation
        start_time_translation = time.perf_counter()

        # Create a single batch payload for all words
        payload = {"q": deduplicated_words, "source": "en", "target": target_language}
        logging.info(f"Batch translating words with payload: {payload}")

        # Make a single POST request for the batch
        response = requests.post(localURL, json=payload, headers={"Content-Type": "application/json"})
        
        if response.status_code == 200:
            # Extract translations for all words
            translations = response.json().get("translatedText", [])
            translated_words = [
                {"originalWord": word, "translatedWord": translation}
                for word, translation in zip(deduplicated_words, translations)
            ]
        else:
            logging.error(f"Batch translation error: {response.text}")
            return jsonify({"error": "Batch translation failed", "details": response.text}), 500

        # Log timing for translation
        logging.info(f"Total time for batch translation: {time.perf_counter() - start_time_translation:.2f} seconds.")

        # Prepare and return the response
        response_data = {"words": translated_words, "targetLanguage": target_language}
        logging.info(f"Batch translation response: {response_data}")
        return jsonify(response_data), 200

    except Exception as e:
        logging.critical(f"Unexpected server error: {str(e)}")
        return jsonify({"error": "Unexpected server error", "details": str(e)}), 500

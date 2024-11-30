
from app import app
from flask import jsonify, request
import requests


# app.route are decorators 
# which modifies the fuctipon that follows it 
# common pattern with decorators is to use them to register functions as call backs for certain events
# decorator below uses association between URL given as an argument and the function
@app.route('/')
@app.route('/index')

def index():
    return "Welcome to Nish's Translation API - where you give us your text, and we'll do the rest!"

def validate_request_data(data):
    required_keys = ('q', 'source', 'target')
    return data and all(key in data and data[key] for key in required_keys)

@app.route('/translate', methods=['POST'])
def translate():
    try: 
        localURL = "http://localhost:5002/translate"  # Docker LibreTranslate URL
        
        # Parse incoming JSON request data
        data = request.get_json()

        # Validate the data before proceeding
        if not validate_request_data(data):
            return jsonify({"error": "Missing or empty required fields"}), 400
        
        # Prepare the payload
        myObj = {
            "q": data.get("q"), 
            "source": data.get("source"),
            "target": data.get("target"),
        }

        # Make the request to LibreTranslate
        response = requests.post(
            localURL, 
            json=myObj,
            headers={"Content-Type": "application/json"}
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Return the translated text as JSON
        return jsonify(response.json()), response.status_code

    except requests.RequestException as e:
        # Catch errors and return a 500 response with details
        return jsonify({"error": "Translation service error", "details": str(e)}), 500

        

# TLDR - Route definition. Where the magic happens...
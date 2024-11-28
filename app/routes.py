
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
    return "Welcome to Nish's Translation API"

@app.route('/translate', methods=['POST'])
def translate():

    data = request.get_json()

    response = requests.post(
        "https://libretranslate.com/translate",
        json={
            "q": data.get("q"),
            "source": data.get("source"),
            "target": data.get("target"),
        },
        headers={"Content-Type": "application/json"},
    )

    # Return LibreTranslate's response as JSON
    return jsonify(response.json())
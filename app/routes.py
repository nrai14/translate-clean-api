
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

def validate_request_data(data):
    required_keys = ('q', 'source', 'target')
    return data and all(key in data for key in required_keys)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()

    if not validate_request_data(data):
        return jsonify({"error": "Missing required fields"}), 400 
    return jsonify({"message": "Validation passed!", "data": data})

# TLDR - Route definition. Where the magic happens...
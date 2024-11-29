
from app import app
from flask import jsonify, request
import requests
import pandas as pd

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
    return data and all(key in data for key in required_keys)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()

    if not validate_request_data(data):
        return jsonify({"error": "Missing required fields"}), 400 
    return jsonify({"message": "Validation passed!", "data": data})

@app.route('/extract', methods=['GET'])
def extract():
    try:
        # Read the Excel file using pandas
        # Added header=None because pandas kept thinking zoom was first cell
        df = pd.read_excel("wordsToTranslate.xlsx", engine='openpyxl', header=None)
        # Get the first cell (A1) value
        a1 = df.iloc[0, 0]
        return jsonify({"Result": a1})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    




# TLDR - Route definition. Where the magic happens...
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib
import json
from pandas import json_normalize
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

#python -m flask --debug run

@app.route('/')
def starting():
    return "Hello world of inteligent systems"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
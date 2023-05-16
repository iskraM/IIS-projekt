from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

#python -m flask --debug run


API_URL = "https://api-inference.huggingface.co/models/devMinty/iis-pet-classifier"
headers = {"Authorization": "Bearer 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"}

@app.route('/')
def starting():
    return "Hello world of inteligent systems"

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No image found", 400
    
    image = request.files['image']
    image_bytes = image.read()

    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
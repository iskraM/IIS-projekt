from flask import Flask, request
from flask_cors import CORS
import requests
from pymongo import MongoClient
from datetime import datetime

#python -m flask --debug run

#region CONFIG
client = MongoClient('mongodb+srv://test123:test123@cluster0.zy8ouhh.mongodb.net/?retryWrites=true&w=majority')
db = client.IISprojekt
zivali = db.zivali

API_URL = "https://api-inference.huggingface.co/models/devMinty/iis-pet-classifier"
headers = {"Authorization": "Bearer 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"}
#endregion

app = Flask(__name__)
CORS(app)

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

@app.route('/feedback', methods=['POST'])
def add_feedback():
    image = request.files['image'].read()
    predicted_label = request.form['predicted_label']
    true_label = request.form['true_label']
    description = request.form['description']
    time = datetime.now()
 
    if not image or not predicted_label or not description: 
        return "Missing data", 400

    zivali.insert_one({
        'image': image,
        'predicted_label': predicted_label,
        'true_label': true_label if true_label else predicted_label,
        'description': description,
        'time': time
    })

    return "Thank you!", 201


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

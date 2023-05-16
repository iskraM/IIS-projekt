from flask import Flask, request
from flask_cors import CORS
import requests
from bson import json_util
from bson.objectid import ObjectId
from pymongo import MongoClient


app = Flask(__name__)

CORS(app)

#python -m flask --debug run

#add mongo connection

client = MongoClient('mongodb+srv://test123:test123@cluster0.zy8ouhh.mongodb.net/?retryWrites=true&w=majority')
db = client.IISprojekt

zivali = db.zivali


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

@app.route('/zivali', methods=['POST'])
def add_zivali():


    #zivali.insert_one({'image': image_bytes,'prediction':})
    return null


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

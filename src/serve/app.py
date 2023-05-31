import os
import time
import json
import openai
import requests

from flask_cors import CORS
from datetime import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, request, jsonify

from dotenv import load_dotenv

import torch
from transformers import AutoImageProcessor, ViTForImageClassification
from PIL import Image
from io import BytesIO

load_dotenv()

#python -m flask --debug run

#region CONFIG
client = MongoClient(os.getenv("MONGODB_URL"))
db = client.IISprojekt
zivali = db.zivali

API_URL = "https://api-inference.huggingface.co/models/devMinty/iis-pet-classifier"
headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_TOKEN')}"}

openai.api_key = os.getenv("OPEN_AI_TOKEN")

#endregion

app = Flask(__name__)
CORS(app)

# model
image_processor = AutoImageProcessor.from_pretrained("devMinty/iis-pet-classifier")
model = ViTForImageClassification.from_pretrained("devMinty/iis-pet-classifier")


def generate_anwser(question):
    responce = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = question,
        max_tokens = 64,
        temperature = 0.7,
        n=1,
        stop = None,
        timeout = 1000,
    )
    anwser = responce.choices[0].text.strip()
    return anwser



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

    # zbudim server
    if "error" in str(response.content):
        time.sleep(20)

        response = requests.post(API_URL, headers=headers, data=image_bytes)

    ff = openai_fun_fact(response.json()[0]['label'])

    prediction =  response.json()[0]
    answer = json.loads(ff.response[0].decode())["anwser"]
    prediction["fun_fact"] = answer

    return prediction, 200

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

@app.route('/aitest/<question>', methods=['POST'])
def openai_fun_fact(question):
    q = "Tell me a fun fact about " + question
    anwser = generate_anwser(q)
    return jsonify({'anwser': anwser})


@app.route('/test_local_model', methods=['POST'])
def test_local_model():    
    if 'image' not in request.files:
        return "No image found", 400
    
    image = request.files['image']
    image_bytes = Image.open(image)

    inputs = image_processor(image_bytes, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_label = logits.argmax(-1).item()
    predicted_class = model.config.id2label[predicted_label]

    ff = openai_fun_fact(predicted_class)

    prediction = {"label": predicted_class}
    answer = json.loads(ff.response[0].decode())["anwser"]
    prediction["fun_fact"] = answer

    return prediction, 200


# region WIKI   
# @app.route('/wikitest/<animal>', methods=['POST'])
# def wikitest(animal):
#     url = "https://en.wikipedia.org/wiki/" + animal
#     if requests.get(url).status_code != 200:
#         return jsonify({'paragraph': "No information found for used search parameter"})
#     else:
#         response = requests.get("https://en.wikipedia.org/wiki/" + animal)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         paragraphs = soup.find_all('p')

#         for paragraph in paragraphs:
#             if animal in paragraph.get_text():
#                 paragraph_text = paragraph.get_text()
#                 paragraph_text = paragraph_text.replace('\n', '')
#                 paragraph_text = paragraph_text.replace('[1]', '')
#                 paragraph_text = paragraph_text.replace('[2]', '')
#                 paragraph_text = paragraph_text.replace('[3]', '')
#                 paragraph_text = paragraph_text.replace('[4]', '')
#                 paragraph_text = paragraph_text.replace('[5]', '')
#                 paragraph_text = paragraph_text.replace('[6]', '')
#                 break
#             elif "_" in animal:
#                 wordeOne = animal.split("_")[0]
#                 if wordeOne in paragraph.get_text():
#                     paragraph_text = paragraph.get_text()
#                     paragraph_text = paragraph_text.replace('\n', '')
#                     paragraph_text = paragraph_text.replace('[1]', '')
#                     paragraph_text = paragraph_text.replace('[2]', '')
#                     paragraph_text = paragraph_text.replace('[3]', '')
#                     paragraph_text = paragraph_text.replace('[4]', '')
#                     paragraph_text = paragraph_text.replace('[5]', '')
#                     paragraph_text = paragraph_text.replace('[6]', '')
#                     break
#             elif " " in animal:
#                 wordeOne = animal.split(" ")[0]
#                 if wordeOne in paragraph.get_text():
#                     paragraph_text = paragraph.get_text()
#                     paragraph_text = paragraph_text.replace('\n', '')
#                     paragraph_text = paragraph_text.replace('[1]', '')
#                     paragraph_text = paragraph_text.replace('[2]', '')
#                     paragraph_text = paragraph_text.replace('[3]', '')
#                     paragraph_text = paragraph_text.replace('[4]', '')
#                     paragraph_text = paragraph_text.replace('[5]', '')
#                     paragraph_text = paragraph_text.replace('[6]', '')
#                     break
#             else:
#                 paragraph_text = "No information found"
        
#         return jsonify({'paragraph': paragraph_text})
# endregion


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

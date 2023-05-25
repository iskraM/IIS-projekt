import os
import json

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

url = os.getenv("MONGODB_URL")
print(f"URL: {url}")

client = MongoClient("mongodb+srv://test123:test123@cluster0.zy8ouhh.mongodb.net/?retryWrites=true&w=majority")
db = client.IISprojekt
collection_zivali = db.zivali

# get all entries from db
all_entries = collection_zivali.find()

# calculate percent of entries that have matching values of prediction and dejanska_zival
correct = 0
count = 0
for entry in all_entries:
    count += 1
    if entry['true_label'] == entry['predicted_label']:
        correct += 1
    
print(f"{correct} out of {count} are correct: {correct/count*100}%")



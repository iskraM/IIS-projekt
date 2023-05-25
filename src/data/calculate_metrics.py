import os
import json
import mlflow

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_url = os.getenv("MONGODB_URL")
mlflow_url = os.getenv("MLFLOW_TRACKING_URI")

client = MongoClient(mongo_url)
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


mlflow.set_tracking_uri(mlflow_url)    
mlflow.set_experiment("DAILY_METRICS_EXPERIMENT")

mlflow.log_metric("Accuracy", correct/count)
mlflow.log_param("All predictions", count)
mlflow.log_param("Correct predictions", correct)
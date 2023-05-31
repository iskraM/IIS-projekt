import os
import cv2
import numpy as np
import pandas as pd
from sklearn import svm
from pymongo import MongoClient
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv

load_dotenv()

mongo = os.getenv("MONGODB_URL")
print(mongo)
client = MongoClient(mongo)


db = client.IISprojekt
zivali = db.zivali

cursor = zivali.find({}, {"image": 1, "true_label": 1})

images = []
labels = []

for document in cursor:
    images.append(document["image"])
    labels.append(document["true_label"])


processed_images = []
for image_str in images:
    # Convert image string to numpy array
    nparr = np.frombuffer(image_str, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Resize the image to a fixed size (e.g., 224x224)
    img_resized = cv2.resize(img, (224, 224))

    # Scale the pixel values between 0 and 1
    img_flattened = img_resized.flatten()

    # Store the preprocessed image
    processed_images.append(img_flattened)


X = np.array(processed_images)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = svm.SVC()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
predictions = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, predictions)

# Print the accuracy
print("Accuracy:", accuracy)
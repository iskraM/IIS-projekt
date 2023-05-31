<div align="center">
    <img alt="Poetry" src="https://img.shields.io/badge/Poetry-fff?style=for-the-badge&logo=poetry">
    <img alt="Poetry" src="https://img.shields.io/badge/scikit learn-fff?style=for-the-badge&logo=scikitlearn">
    <img alt="Poetry" src="https://img.shields.io/badge/mlflow-fff?style=for-the-badge&logo=mlflow">
    <img alt="Poetry" src="https://img.shields.io/badge/dvc-fff?style=for-the-badge&logo=dvc">
    <img alt="Python" src="https://img.shields.io/badge/Python-fff?style=for-the-badge&logo=python">
    <img alt="Python" src="https://img.shields.io/badge/Vue.js-fff?style=for-the-badge&logo=vue.js">
    <img alt="Postman" src="https://img.shields.io/badge/Docker-fff?style=for-the-badge&logo=docker"/>
    <img alt="Postman" src="https://img.shields.io/badge/Postman-fff?style=for-the-badge&logo=postman"/>
</div>

# Petster 2000
Pet Classifier with Fun Facts.

## Description
This project consists of an API, a website, and daily workflows designed to provide users with a fun and interactive experience related to pets. The core functionality of the project is a machine learning (ML) classifier that predicts the type of pet in an uploaded image and retrieves fun facts about the predicted pet using the OpenAI model.

## API
The API serves as the backbone of the project and hosts the ML classifier. It receives an image of a pet as input and returns the prediction of the pet's type. Additionally, it leverages the power of the OpenAI model to generate interesting and entertaining fun facts about the predicted pet. The API acts as the bridge between the ML model and the website, enabling seamless communication and data transfer.

## Website
The website is the user-facing component of the project, providing a user-friendly interface for interacting with the ML classifier and accessing pet predictions and fun facts. Users can upload an image of their pet through the website, and the API will process the image, providing the predicted pet type along with engaging and informative fun facts. Furthermore, the website allows users to provide feedback on the accuracy of the model's predictions, enhancing the system's learning and improving its performance over time.

## Workflows
The project incorporates two daily workflows to ensure the smooth operation and continuous improvement of the system:

1. Daily Metrics Workflow: This workflow collects and analyzes daily metrics related to the production model. It helps monitor the performance of the ML classifier, providing valuable insights into its accuracy, response time, and other relevant metrics. These metrics assist in identifying areas of improvement and optimizing the overall user experience.

2. Continuous Training Workflow: This workflow focuses on the continuous training of the ML model. It leverages new data to retrain the model periodically, ensuring it remains up-to-date and capable of accurate predictions. By incorporating newly available information, the model can adapt to changing trends and improve its prediction capabilities over time.

## Instalation and Setup
To run the project locally using Docker Compose, follow these steps:

1. Pull the repository
2. Navigate to the project directory
3. Open the `docker-compose.yml` and set up the required environment variables
4. Run the following command to pull the docker images and setup the containers
```
docker compose up -d
```
5. Once you have the containers up and running, you can access the website by opening your web browser and navigating to `http:/localhost:8080`

## Contributors
This project was developed as a collaborative effort for our Master's assignment in Engineering of Intelligent Systems (IIS). We, Marcel and Aljaž, worked together to conceptualize, and implement this project.

<table>
    <tbody>
        <tr>
            <td align="center">
                <a href="https://github.com/iskraM">
                    <img src="https://avatars.githubusercontent.com/u/40259973?v=4" width="100px;" alt="Marcel Iskrač Github avatar"/>
                    <br/>
                    <sub><b>Marcel Iskrač</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/LiparAljaz">
                    <img src="https://avatars.githubusercontent.com/u/59646484?v=4" width="100px;" alt="Aljaž Lipar Github avatar"/>
                    <br/>
                    <sub><b>Aljaž Lipar</b></sub>
                </a>
            </td>
        </tr>
    </tbody>
</table>

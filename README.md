# Docker Init Example

This repository contains Docker utility files generated by `docker init`, demonstrating how to initialize and configure a Docker environment for a Python project using FastAPI.

## Background

This project was created as part of a tutorial aimed at showing the use of `docker init` to simplify the dockerization of applications. The example focuses on a fictional rent prediction application. **It's important to note that no real machine learning model is implemented here.** Instead, we use a simulated prediction function based on a dictionary to illustrate how a model could be deployed and containerized easily with `docker init`.

## Project Structure

- `main.py`: The entry point for the FastAPI application, including a welcome endpoint and a dummy prediction endpoint.
- `ml.py`: Module containing the dummy prediction function.
- `requirements.txt`: The python packages to install

## How to Use
### Clone this repository using : 
```bash
git clone https://github.com/bricefotzo/docker-init-example.git
```

### Generate docker resources:
1. Navigate to the project directory: `cd docker-init-example`.
2. Run the command `docker init`
3. Answer the 4 questions. 
    - What application platform does your project use?   
    - What version of Python do you want to use?
    - What port do you want your app to listen on?
    - What is the command you use to run your app?
>You'll notice that docker inferred the langage, and the right command to execute.

### To run the application:

1. Launch the application with Docker Compose: `docker compose up`.
2. Access the application through your browser at `http://localhost:8000`.

To test the prediction endpoint:

- Use a GET request at `http://localhost:8000/predict?city=Paris&rooms=1&area=20`.

## Disclaimer

This project is purely educational and intended to illustrate the use of `docker init` in the context of deploying FastAPI applications. The prediction function used here is fictional and should not be considered as an example of an operational machine learning model.


"""
This module contains the API for rent prediction.
"""
from fastapi import FastAPI
from ml import predict_rent

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to rent prediction API!"}

@app.get("/tree")
async def tree(folder_name: str):
    import os
    return {
            "tree": os.listdir(folder_name)
        }

@app.get("/predict")
async def prediction(city: str, rooms: int, area: float):
    return {
            "predicted_rent": predict_rent(city, rooms, area), 
            "devise": "euros"
        }

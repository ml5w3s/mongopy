from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# create a new collection
collection = db["mycollection"]

document = {"name": "John", "age": 30}

result = collection.insert_one(document)
print(result.inserted_id)

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    result = collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}
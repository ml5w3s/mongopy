from fastapi import FastAPI
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]

# Asynchronously connect to the MongoDB server using Motor
async_client = AsyncIOMotorClient("mongodb://localhost:27017")
async_db = async_client["mydatabase"]

# Create a new document
@app.post("/users")
async def create_user(user: dict):
    result = await async_db.users.insert_one(user)
    return {"user_id": str(result.inserted_id)}

# Read a document by ID
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    user = await async_db.users.find_one({"_id": ObjectId(user_id)})
    return user

# Update a document by ID
@app.put("/users/{user_id}")
async def update_user(user_id: str, user: dict):
    result = await async_db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user})
    return {"modified_count": result.modified_count}

# Delete a document by ID
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    result = await async_db.users.delete_one({"_id": ObjectId(user_id)})
    return {"deleted_count": result.deleted_count}

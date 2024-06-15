import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb+srv://harishscc123:S97r3Gdja1JA60PH@forms.ejlqcyb.mongodb.net/?retryWrites=true&w=majority&appName=Forms")

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client.typeform
forms_collection = database.get_collection("forms")

async def get_db():
    return forms_collection

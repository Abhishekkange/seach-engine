import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os

load_dotenv()

mongo_url = os.environ.get('MONGO_URL')
gemini_api_key = os.environ.get('GEMINI_API_KEY')

def dbconnect(uri):
    conn = MongoClient(uri)
    print("Connected to database")
    return conn

def embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=gemini_api_key)
    return embeddings

def generate_embeddings(text):
    embeddings_instance = embeddings()
    embeded_data = embeddings_instance.embed_documents(text)
    return embeded_data

def getSearchResults(query, collection,index):
   results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embeddings(query),
    "path": "titleEmbedding",
    "numCandidates": 100,
    "limit": 2,
    "index": "vector_ind",
      }}
    ])
   return results
    

# Main
client = dbconnect(mongo_url)
db = client["KangeCollection"]
collection = db["products"]

#creating vector here 
# documents = collection.find().limit(6)
#     # Loop through each document
# for doc in documents:
#         # Generate vector embedding for the text in the document
#     embedding = generate_embeddings(doc["name"].get("en"))
#         # Add the vector embedding to the document under a new key "vector_embedding"
#     doc["titleEmbedding"] = embedding
#         # Update the document in the collection
#     collection.update_one({"_id": doc["_id"]}, {"$set": {"titleEmbedding": embedding}})


# search query here
data = getSearchResults("blue", collection,"vector_ind",2)
documents = list(data)
for doc in documents:
    print(doc["name"].get("en"))

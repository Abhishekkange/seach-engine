from query_parser import getSearchResults
from utilities import dbconnect
from vectorizer import vectorize

import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os

load_dotenv()

mongo_url = os.environ.get('MONGO_URL')
gemini_api_key = os.environ.get('GEMINI_API_KEY')
# Main
client = dbconnect(mongo_url)
db = client["KangeCollection"]
collection = db["products"]

documents = collection.find().limit(3)

for doc in documents:
    vectorize(collection,doc)





# documents = getSearchResults("dres mtial",collection,index="vector_ind",limit=2)

# for doc in documents:
#     print(doc["name"].get("en"))
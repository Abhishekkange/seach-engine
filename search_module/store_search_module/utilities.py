import pymongo
from pymongo import MongoClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os


def dbconnect(mongo_url):
    conn = MongoClient(mongo_url)
    print("Connected to database")
    return conn

def embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="AIzaSyANqyvxOpFeKyVjDI_fbkTGp2aaKYu_MS4")
    return embeddings

def generate_embeddings(text):
    embeddings_instance = embeddings()
    embeded_data = embeddings_instance.embed_documents(text)
    return embeded_data
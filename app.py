from query_parser import getSearchResults
from utilities import dbconnect
from vectorizer import vectorize
import pymongo
from pymongo import MongoClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from bson import ObjectId
from bson import json_util
import json
from flask import Flask,jsonify,request


app = Flask(__name__)




# Set the environment variable to prevent bytecode generation
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'


# Main
client = dbconnect("mongodb+srv://NearbyKart_production:vgDxWwhHwhdWkSO0@cluster0.nkwn8jm.mongodb.net/")
# db = client["KangeCollection"]
# collection = db["products"]

# documents = collection.find().limit(3)

# for doc in documents:
#     vectorize(collection,doc)

@app.route("/", methods=['GET'])
def start_server():
    return "server running"

@app.route("/searchstore", methods=['POST'])
def search():

    data = request.json
    database = data.get('storeId')
    query = data.get('query')
    index = data.get('index')
    limit = data.get('limit')

    # get required collection 
    db = client[database]
    collection = db["products"]
    result = getSearchResults(query=query,collection=collection,limit=limit,index=index)

    result_list = list(result)
    json_documents = json_util.dumps(result_list)
    # json_documents = [json.dumps(doc, default=json_util.default) for doc in result_list]

   

    return json_documents


@app.route("/searchindexing", methods=['POST'])
def index_documents():

    data = request.json
    ids = data.get('list')
    id_list = list(ids)
    database = data.get('storeId')  # Use 'storeId' as the key to retrieve the database name from the JSON data
    db = client[database]
    collection = db["products"]

    for doc_id in id_list:
        document = collection.find_one({"_id": ObjectId(doc_id)})
        type(document)
        vectorize(collection,document)
    
    return "completed"

if __name__ == '__main__':
    app.run(debug=True)

#main here

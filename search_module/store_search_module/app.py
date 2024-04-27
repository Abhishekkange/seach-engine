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





# documents = getSearchResults("dress",collection,index="vector_ind",limit=3)

# for doc in documents:
#     print(doc["name"].get("en"))

#Routes here 
def convert_ids_to_string(documents):
    for i, doc in enumerate(documents):
        # Check if '_id' field exists in the document
        if '_id' in doc:
            # Convert '_id' field to string
            doc['_id'] = str(doc['_id'])
        else:
            print(f"Document {i} does not have an '_id' field.")
        # If categories exist, convert category _id fields to string
        if 'categories' in doc:
            for j, category in enumerate(doc['categories']):
                if '_id' in category:
                    category['_id'] = str(category['_id'])
                else:
                    print(f"Category {j} in document {i} does not have an '_id' field.")
        # If subcategories exist, convert subcategory _id fields to string
        if 'subcategories' in doc:
            for k, subcategory in enumerate(doc['subcategories']):
                if '_id' in subcategory:
                    subcategory['_id'] = str(subcategory['_id'])
                else:
                    print(f"Subcategory {k} in document {i} does not have an '_id' field.")


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

#main here

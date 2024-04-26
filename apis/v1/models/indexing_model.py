from flask import request , jsonify
from vectorizer import vectorize
import os


def start_indexing_mod(ids,database):

    client = dbconnect()
    db = client[database]
    collection = db["products"]

    for id in ids:

        #finding the required document
        document_id = ObjectId(id)
        document = collection.find_one({'_id': document_id})
        #vectorize this document
        vectorize(collection,document)
    return




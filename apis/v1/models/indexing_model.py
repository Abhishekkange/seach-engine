from flask import request , jsonify
from ..search_module.store_search_module.vectorizer import vectorize
from ..search_module.store_search_module.utilities import dbconnect
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




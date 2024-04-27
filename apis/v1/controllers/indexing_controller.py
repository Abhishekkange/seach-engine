from flask import request,jsonify,current_app
from ..models.indexing_model import start_indexing_mod

#dao
#services
#view

@current_app.get('/')
def starter():
    return "Server is running"

@app.post('/start-indexing')
def start_indexing():

    data = request.json()
    ids = data.get('ids')
    database = data.get('storeId')

    return start_indexing_mod(ids,database)
from app import app
from Flask import request,jsonify
from models.indexing_model import start_indexing_mod


@app.post('/start-indexing')
def start_indexing():

    data = request.json()
    ids = data.get('ids')
    database = data.get('storeId')

    return start_indexing_mod(ids,database)
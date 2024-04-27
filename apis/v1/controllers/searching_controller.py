
from Flask import jsonify
import app as app

@app.get('/search/<query>')
def search(query):

    data = request.json()
    index = data.get('index')
    database = data.get('storeId')

    result = search_mod(query,database,index,limit).jsonify()
    return result

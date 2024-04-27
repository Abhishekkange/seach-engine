from query_parser import getSearchResults
from utilities import dbconnect

def search_mod(query,database,index,limit):

    client = dbconnect()
    db = client[database]
    collection = db["products"]

    result = getSearchResults(query,collection=collection,limit=limit,index=index)
    return result

abc = search_mod('dress')
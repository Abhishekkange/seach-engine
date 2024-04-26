from query_parser import getSearchResults

def search_mod(query):

    result = getSearchResults(query)
    return result

abc = search_mod('dress')
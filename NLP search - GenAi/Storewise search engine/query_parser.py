from utilities import generate_embeddings



def getSearchResults(query, collection,index,limit=5):
   results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embeddings(query),
    "path": "titleEmbedding",
    "numCandidates": 100,
    "limit": limit,
    "index": index,
      }}
    ])
   return list(results)
   

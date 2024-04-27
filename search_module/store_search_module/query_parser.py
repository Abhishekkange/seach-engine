from utilities import generate_embeddings



def getSearchResults(query, collection,index,limit=5):
     results = collection.aggregate([
        {"$vectorSearch": {
            "queryVector": generate_embeddings(query),
            "path": "titleEmbedding",
            "numCandidates": 100,
            "limit": limit,
            "index": index,
        }},
        {"$project": {
            "_id": 1,  # Exclude _id field from top-level document
            "name": 1,
            "categories": {
                "$map": {
                    "input": "$categories",
                    "as": "category",
                    "in": {
                        "categoryName": "$$category.categoryName",
                        "categoryImage": "$$category.categoryImage"
                    }
                }
            },
            "subcategories": {
                "$map": {
                    "input": "$subcategories",
                    "as": "subcategory",
                    "in": {
                        "subcategoryName": "$$subcategory.subcategoryName",
                        "subcategoryImage": "$$subcategory.subcategoryImage"
                    }
                }
            },
            "price": 1,
            "shopName": 1,
            "shortDescription": 1,
            "description": 1,
            "image": 1,
            "reviews": 1,
            "details": 1,
            "__v": 1
        }}
    ])
    
     return results
   

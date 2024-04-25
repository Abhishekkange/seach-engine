#This module deals with generating the Vectors of given Documents from a given datanbase and collection
from utilities import generate_embeddings



def vectorize(collection,document):
    title = document["name"].get("en")
    category = document["categories"][0].get("categoryName").get("en")
    subcategory = document["subcategories"][0].get("subcategoryName").get("en")
    description = document["description"].get("en")
    shortDescription = document["shortDescription"].get("en")
    price = document["price"]
    text = ""
    text =text + title+" "+ description +" "+ shortDescription+""+""+ category +""+subcategory
    print(text)
    embedding = generate_embeddings(document["name"].get("en"))
# Add the vector embedding to the document under a new key "vector_embedding"
    document["titleEmbedding"] = embedding
# Update the document in the collection
    collection.update_one({"_id": doc["_id"]}, {"$set": {"titleEmbedding": embedding}})
    return

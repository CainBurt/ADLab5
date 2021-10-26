from pymongo import MongoClient
from bson.json_util import dumps


def get_mongodb_items():
    cluster = MongoClient("mongodb+srv://cain:Password12@advanceddevelopment.tz0f9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
    db = cluster["PythonTest"]
    collection = db["Students"]

    myCursor = None

    # create queries

    title_query = {"Unit title": {"$eq": "AD Unit"}}

    author_query = {"Unit leader": {"$eq": "Xin"}}

    dateCreated_query = {"dateCreated": {"$eq": 2021}}

    myCursor = collection.find({"$and": [title_query, author_query, dateCreated_query]})



    list_cur = list(myCursor)
    print(list_cur)

    json_data = dumps(list_cur)



    return json_data


get_mongodb_items()
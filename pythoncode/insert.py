import pymongo
from pymongo import MongoClient

#had to add &ssl=true&ssl_cert_reqs=CERT_NONE to the end to make it work
cluster=MongoClient("mongodb+srv://cain:Password12@advanceddevelopment.tz0f9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
db=cluster["PythonTest"]
collection=db["Students"]

post1={"_id":1, "name": "Lucas","score":5}
post2={"_id":2, "name": "Daniel","score":5}
collection.insert_many([post1,post2])
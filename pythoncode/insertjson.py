from pymongo import MongoClient

def store_post_mongodb(Unittitle, Unitleader, content, dateCreated, thumbnail):

  cluster = MongoClient("mongodb+srv://cain:Password12@advanceddevelopment.tz0f9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
  db = cluster["PythonTest"]
  collection = db["Students"]


  # use (uncomment) the following line to add an item programmatically to the collection.
  json_data = {"Unit title": Unittitle, "Unit leader": Unitleader, "dateCreated": dateCreated, "thumbnail": thumbnail, "content": content}
  collection.insert_one(json_data)


store_post_mongodb('AD Unit','Xin','Welcome to Advanced Unit',2021,',')
store_post_mongodb('WP Unit','Xin','Web programming',2021,',')
from math import e
from pymongo import MongoClient




from fastapi import FastAPI,Response

app = FastAPI()
@app.get("/")
def test():
    print("Home")
    return "Home"
@app.get("/db")
def db():

    try:


        # client = MongoClient("mongodb://root:MongoFresh123@10.201.1.160:27017/")
        client = MongoClient("mongodb://wikiSupport:W!k!Support%40!23@10.105.0.31:27017/")
        

        db = client['wikiSupport']



        collection = db['Articles']


        document = collection.find_one()

        print(document)

        # response = Response(content=document, media_type="text/html")

        return "Success"
    except Exception as e:
        return str(e)
    

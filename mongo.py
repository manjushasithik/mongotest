from pymongo import MongoClient




from fastapi import FastAPI,Response

app = FastAPI()
@app.get("/")
def test():
    print("Home")
    return "Home"
@app.get("/db")
def db():


# client = MongoClient("mongodb://paladmin:Administrator$Mariapp@10.201.1.181:27017/")

    client = MongoClient("mongodb://root:MongoFresh123@10.201.1.160:27017/")
    print("client =========",client)
    db = client['Wiki_DEVDB']



    collection = db['Articles']


    document = collection.find_one()

    print(document)

    # response = Response(content=document, media_type="text/html")

    return "Success"

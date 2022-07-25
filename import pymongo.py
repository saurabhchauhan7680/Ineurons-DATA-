import pymongo
client = pymongo.MongoClient("mongodb+srv://SauravChauhan:lalaland@atlascluster.2d89jje.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" :"saurav",
    "email" :"ahsjkkjhjk.gmail",
    "surname" :"Chauhan"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d )



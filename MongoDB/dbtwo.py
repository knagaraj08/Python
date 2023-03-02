import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]



# this fetches all the record 
# for _ in mycol.find():
#     print(_)


# this prints only the initail record
# x = mycol.find_one()
# print(x)

for x in mycol.find({}, {"name":1,"address":1 }):
    print(x)
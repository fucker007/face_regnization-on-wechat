#!/usr/bin/python3

import pymongo

# myclient = pymongo.MongoClient("mongodb://model:model@106.14.200.68:27017/")
myclient = pymongo.MongoClient("mongodb://106.14.200.68:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)
print(x)
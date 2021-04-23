from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]
clients = db["Clients"]
factura= db["Factura"]

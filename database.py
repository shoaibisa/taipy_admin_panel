import pymongo
from dotenv import load_dotenv
import os
from taipy.gui import notify
import pandas as pd

load_dotenv()


client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client["GoShop"]
collection_product = db["products"]


def insert_one_collection(document):
    return collection_product.insert_one(document)


def all_prodcuts():
    cursor = collection_product.find()
    list_cur = list(cursor)
    df = pd.DataFrame(list_cur)
    return df

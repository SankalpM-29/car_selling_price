import pymongo

def establish():

    DEFAULT_CONNECTION_URL = "mongodb+srv://sankalp:mongodb1357@cluster1.tajfw.mongodb.net/cardb?retryWrites=true&w=majority"
    DB_NAME = "cardb"

    # Establish a connection with mongoDB
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

    # Create a DB
    database = client[DB_NAME]

    return database


def update(database, data):

    #creating collection
    COLLECTION_NAME = "cardata"
    collection = database[COLLECTION_NAME]
    response = collection.insert_one(data)
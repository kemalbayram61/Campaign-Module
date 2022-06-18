from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.typings import _DocumentType, Optional
from pymongo.cursor import Cursor

class DBHelper:
    __connectionString: str = None
    __dbname: str = None
    __mongoClient: MongoClient = None
    __database: Database[_DocumentType] = None
    def __init__(self, connectionString: str, dbName: str):
        self.__connectionString = connectionString
        self.__dbname = dbName
        clientCase:bool = self.setClient()
        if(clientCase):
            databaseCase:bool = self.setDatabase()
            if(databaseCase == False):
                raise Exception("Database name is invalid.")
        else:
            raise Exception("Connection string is invalid.")

    def setClient(self) ->bool:
        if(self.__connectionString != None):
            self.__mongoClient = MongoClient(self.__connectionString)
            return True
        return False

    def setDatabase(self) ->bool:
        if(self.__mongoClient != None):
            self.__database = self.__mongoClient.get_database(self.__dbname)
            return True
        return False

    def getCollection(self, collectionName: str) ->Collection:
        return self.__database.get_collection(collectionName)

    def insertOne(self, collectionName: str, document) ->bool:
        collection = self.getCollection(collectionName)
        if(collection != None):
            collection.insert_one(document)
            return True
        return False

    def insertMany(self, collectionName: str, documentList) ->bool:
        collection = self.getCollection(collectionName)
        if(collection != None):
            collection.insert_many(documentList)
            return True
        return False

    def getDocuments(self, collectionName: str, filter:dict) ->Cursor[_DocumentType]:
        return self.getCollection(collectionName).find(filter)

    def getDocument(self, collectionName: str, filter: dict) ->Optional[_DocumentType]:
        return self.getCollection(collectionName).find_one(filter)
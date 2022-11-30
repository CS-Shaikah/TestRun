import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            # TODO1: Update with appropriate MongoDB connection information
            url = "mongodb://dbproject2:K3waiQwhLJ1WQAVy4ONvNvBAx9hJLle5LIi3SrMTE7GGp9TRVbFIeXEI2Bg3QXwyM76TC6von96UACDbU9Mx6g==@dbproject2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@dbproject2@"
            client = pymongo.MongoClient(url)
            database = client['dbproject2']
            collection = database['advertisements']

            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)

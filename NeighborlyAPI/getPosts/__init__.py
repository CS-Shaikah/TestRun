import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # TODO1: Update with appropriate MongoDB connection information
        url = "mongodb://dbproject2:K3waiQwhLJ1WQAVy4ONvNvBAx9hJLle5LIi3SrMTE7GGp9TRVbFIeXEI2Bg3QXwyM76TC6von96UACDbU9Mx6g==@dbproject2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@dbproject2@"
        client = pymongo.MongoClient(url)
        database = client['cosmos-neighborly-dev']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)

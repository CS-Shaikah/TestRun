import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://dbproject2:K3waiQwhLJ1WQAVy4ONvNvBAx9hJLle5LIi3SrMTE7GGp9TRVbFIeXEI2Bg3QXwyM76TC6von96UACDbU9Mx6g==@dbproject2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@dbproject2@"  # TODO1: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['dbproject2']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
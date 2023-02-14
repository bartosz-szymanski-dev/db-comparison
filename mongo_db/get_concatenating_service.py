import time
import mongo_db.collection_helper as collection_helper


def run_benchmark(client):
    print('Benchmark name: MongoDB Get concatenated from two collection')
    data_collection = collection_helper.get_data_collection(client)
    start = time.time()
    pymongo_cursor = data_collection.aggregate([
        {
            "$lookup":
                {
                    "from": "factories",
                    "localField": "make",
                    "foreignField": "name",
                    "as": "factories_data"
                }
        },
        {
            "$match": {
                "factories_data.name": "TESLA",
            },
        }
    ])
    all_data = list(pymongo_cursor)
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows fetched: ', str(len(all_data)))

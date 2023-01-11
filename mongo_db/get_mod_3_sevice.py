import time
import mongo_db.collection_helper as data_collection_helper


# TODO: it's not working - it's fetching all the documents instead of every third
def run_benchmark(client):
    print('Benchmark name: MongoDB Get every 3rd document')
    data_collection = data_collection_helper.get_data_collection(client)
    start = time.time()
    pymongo_cursor = data_collection.find({}).skip(2).limit(1)
    all_data = list(pymongo_cursor)
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows fetched: ', str(len(all_data)))

import time
import mongo_db.collection_helper as data_collection_helper


# TODO: it's not working - it's fetching all the documents instead of every third
def run_benchmark(client):
    print('Benchmark name: MongoDB Get every 3rd document')
    data_collection = data_collection_helper.get_data_collection(client)
    max_number = 112634
    modulo_3_list = [str(number * 3) for number in range(int(max_number / 3))]
    start = time.time()
    pymongo_cursor = data_collection.find({"index": {"$in": modulo_3_list}})
    all_data = list(pymongo_cursor)
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows fetched: ', str(len(all_data)))

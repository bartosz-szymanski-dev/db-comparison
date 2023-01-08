import time
import mongo_db.collection_helper as data_collection_helper


def run_benchmark(client):
    print('Benchmark name: MongoDB Delete All')
    start = time.time()
    delete_result = data_collection_helper.get_data_collection(client).delete_many({})
    print('Query time: ' + str(round(time.time() - start)) + 's')
    print('Documents deleted: ' + str(delete_result.deleted_count))

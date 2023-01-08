import time


def run_benchmark(client):
    print('Benchmark name: MongoDB Get All')
    evp = client['evp']
    data_collection = evp['data']
    start = time.time()
    pymongo_cursor = data_collection.find({})
    all_data = list(pymongo_cursor)
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows fetched: ' + str(len(all_data)))

import time


def run_benchmark(client):
    print('Benchmark name: MySQL Get All')
    start = time.time()
    cursor = client.cursor()
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    all_data = list(result)
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows fetched: ' + str(len(all_data)))

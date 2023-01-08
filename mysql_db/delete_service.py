import time


def run_benchmark(client):
    print('Benchmark name: MySQL Delete All')
    start = time.time()
    cursor = client.cursor()
    cursor.execute("DELETE FROM data")
    client.commit()
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows deleted: ' + str(cursor.rowcount))

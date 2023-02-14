import time


def run_benchmark(client):
    print('Benchmark name: MySQL Get Join')
    start = time.time()
    cursor = client.cursor()
    cursor.execute(
        "SELECT DISTINCT d.* FROM factories as f INNER JOIN data as d on f.name = d.make WHERE f.name = 'TESLA'"
    )
    result = cursor.fetchall()
    all_data = list(result)
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows fetched: ' + str(len(all_data)))

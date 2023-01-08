import time

import csv_import_helper


def run_benchmark(client):
    print('Benchmark name: MySQL Insert All')
    list_to_insert = csv_import_helper.get_list_to_insert(process_row)
    start = time.time()
    cursor = client.cursor()
    cursor.executemany(
        "INSERT INTO data (id, vin, county, city, state, postal_code, model_year, make, model, electric_vehicle_type, "
        "clean_alternative_fuel_vehicle_eligibility, electric_range, base_msrp, legislative_district, dol_vehicle_id, "
        "vehicle_location, electric_utility, census_tract) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
        "%s, %s, %s, %s, %s, %s)",
        list_to_insert
    )
    client.commit()
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows inserted: ' + str(len(list_to_insert)))


def append_to_insert_list(list_to_insert, row):
    list_to_insert.append(row)


def process_row(list_to_insert, row):
    try:
        append_to_insert_list(list_to_insert, row)
    except Exception as error:
        print('[CSV][error] Something went wrong when appending to list: ' + str(error))

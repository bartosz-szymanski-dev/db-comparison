import time
import csv_import_helper
import mongo_db.collection_helper as data_collection_helper


def run_benchmark(client):
    print('Benchmark name: MongoDB Insert All')
    list_to_insert = csv_import_helper.get_list_to_insert(process_row)
    start = time.time()
    data_collection_helper.get_data_collection(client).insert_many(list_to_insert)
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows inserted: ' + str(len(list_to_insert)))


def process_row(list_to_insert, row):
    try:
        append_to_insert_list(list_to_insert, row)
    except Exception as error:
        print('Something went wrong when appending to list: ' + str(error))


def append_to_insert_list(list_to_insert, row):
    list_to_insert.append({
        'vin': row[0],
        'county': row[1],
        'city': row[2],
        'state': row[3],
        'postal_code': row[4],
        'model_year': row[5],
        'make': row[6],
        'model': row[7],
        'electric_vehicle_type': row[8],
        'clean_alternative_fuel_vehicle_eligibility': row[9],
        'electric_range': row[10],
        'base_msrp': row[11],
        'legislative_district': row[12],
        'dol_vehicle_id': row[13],
        'vehicle_location': row[14],
        'electric_utility': row[15],
        'census_tract': row[16],
    })

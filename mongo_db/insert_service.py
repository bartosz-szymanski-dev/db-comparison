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
        'index': row[0],
        'vin': row[1],
        'county': row[2],
        'city': row[3],
        'state': row[4],
        'postal_code': row[5],
        'model_year': row[6],
        'make': row[7],
        'model': row[8],
        'electric_vehicle_type': row[9],
        'clean_alternative_fuel_vehicle_eligibility': row[10],
        'electric_range': row[11],
        'base_msrp': row[12],
        'legislative_district': row[13],
        'dol_vehicle_id': row[14],
        'vehicle_location': row[15],
        'electric_utility': row[16],
        'census_tract': row[17],
    })

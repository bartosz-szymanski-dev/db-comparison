import time

import update_helper
import mongo_db.collection_helper as data_collection_helper


def run_benchmark(client):
    print('Benchmark name: MongoDB Update All')
    start = time.time()
    update_result = data_collection_helper.get_data_collection(client).update_many({}, {
        '$set': {
            'vin': update_helper.get_random_string(),
            'county': update_helper.get_random_string(),
            'city': update_helper.get_random_string(),
            'state': update_helper.get_random_string(),
            'postal_code': update_helper.get_random_string(),
            'model_year': update_helper.get_random_string(),
            'make': update_helper.get_random_string(),
            'model': update_helper.get_random_string(),
            'electric_vehicle_type': update_helper.get_random_string(),
            'clean_alternative_fuel_vehicle_eligibility': update_helper.get_random_string(),
            'electric_range': update_helper.get_random_string(),
            'base_msrp': update_helper.get_random_string(),
            'legislative_district': update_helper.get_random_string(),
            'dol_vehicle_id': update_helper.get_random_string(),
            'vehicle_location': update_helper.get_random_string(),
            'electric_utility': update_helper.get_random_string(),
            'census_tract': update_helper.get_random_string(),
        }
    })
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Documents updated: ' + str(update_result.modified_count))

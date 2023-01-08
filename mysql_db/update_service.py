import time

import update_helper


def run_benchmark(client):
    print('Benchmark name: MySQL Update All')
    start = time.time()
    cursor = client.cursor()
    sql = "UPDATE data SET " \
          "vin = %s, " \
          "county = %s, " \
          "city = %s, " \
          "state = %s, " \
          "postal_code = %s, " \
          "model_year = %s, " \
          "make = %s, " \
          "model = %s, " \
          "electric_vehicle_type = %s, " \
          "clean_alternative_fuel_vehicle_eligibility = %s, " \
          "electric_range = %s, " \
          "base_msrp = %s, " \
          "legislative_district = %s, " \
          "dol_vehicle_id = %s, " \
          "vehicle_location = %s, " \
          "electric_utility = %s, " \
          "census_tract = %s"
    cursor.execute(sql, (
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
        update_helper.get_random_string(),
    ))
    client.commit()
    print('Query time: ' + str(round(time.time() - start, 2)) + 's')
    print('Rows updated: ' + str(cursor.rowcount))

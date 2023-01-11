import mongo_db.connection as connection
import mongo_db.insert_service as mongo_insert_service
import mongo_db.get_service as mongo_get_service
import mongo_db.update_service as mongo_update_service
import mongo_db.delete_service as mongo_delete_service
import mongo_db.get_mod_3_sevice as mongo_get_mod_3_service


def dispatch(chosen_db, chosen_action):
    if chosen_db != '1':
        return

    client = connection.get_connection()
    if chosen_action == '1':
        mongo_insert_service.run_benchmark(client)
    elif chosen_action == '2':
        mongo_get_service.run_benchmark(client)
    elif chosen_action == '3':
        mongo_update_service.run_benchmark(client)
    elif chosen_action == '4':
        mongo_delete_service.run_benchmark(client)
    elif chosen_action == '5':
        mongo_get_mod_3_service.run_benchmark(client)

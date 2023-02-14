import mongo_db.connection as connection
import mongo_db.insert_service as mongo_insert_service
import mongo_db.get_service as mongo_get_service
import mongo_db.update_service as mongo_update_service
import mongo_db.delete_service as mongo_delete_service
import mongo_db.get_mod_3_sevice as mongo_get_mod_3_service
import mongo_db.get_concatenating_service as mongo_concatenating_service


def dispatch(chosen_db, chosen_action):
    if chosen_db != '1':
        return

    action = get_actions()[chosen_action]
    client = connection.get_connection()
    action(client)


def get_actions():
    return {
        '1': mongo_insert_service.run_benchmark,
        '2': mongo_get_service.run_benchmark,
        '3': mongo_update_service.run_benchmark,
        '4': mongo_delete_service.run_benchmark,
        '5': mongo_get_mod_3_service.run_benchmark,
        '6': mongo_concatenating_service.run_benchmark,
    }

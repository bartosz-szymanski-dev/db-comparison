import mysql_db.connection as connection
import mysql_db.insert_service as mysql_import_service
import mysql_db.get_service as mysql_get_service
import mysql_db.update_service as mysql_update_service
import mysql_db.delete_service as mysql_delete_service
import mysql_db.get_mod_3_service as mysql_get_mod_3_service
import mysql_db.get_concatenating_service as mysql_join_service


def dispatch(chosen_db, chosen_action):
    if chosen_db != '2':
        return

    action = get_actions()[chosen_action]
    client = connection.get_connection()
    action(client)


def get_actions():
    return {
        '1': mysql_import_service.run_benchmark,
        '2': mysql_get_service.run_benchmark,
        '3': mysql_update_service.run_benchmark,
        '4': mysql_delete_service.run_benchmark,
        '5': mysql_get_mod_3_service.run_benchmark,
        '6': mysql_join_service.run_benchmark,
    }

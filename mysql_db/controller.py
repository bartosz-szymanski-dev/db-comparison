import mysql_db.connection as connection
import mysql_db.insert_service as mysql_import_service
import mysql_db.get_service as mysql_get_service
import mysql_db.update_service as mysql_update_service
import mysql_db.delete_service as mysql_delete_service
import mysql_db.get_mod_3_service as mysql_get_mod_3_service


def dispatch(chosen_db, chosen_action):
    if chosen_db != '2':
        return

    client = connection.get_connection()
    if chosen_action == '1':
        mysql_import_service.run_benchmark(client)
    elif chosen_action == '2':
        mysql_get_service.run_benchmark(client)
    elif chosen_action == '3':
        mysql_update_service.run_benchmark(client)
    elif chosen_action == '4':
        mysql_delete_service.run_benchmark(client)
    elif chosen_action == '5':
        mysql_get_mod_3_service.run_benchmark(client)

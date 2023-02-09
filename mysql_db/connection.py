import mysql.connector


def create_data_table(mysql_client):
    cursor = mysql_client.cursor()
    cursor.execute(open('./mysql_db/evp.data.sql', 'r').read())
    cursor.execute(open('./mysql_db/evp.factories.sql', 'r').read())


def get_connection():
    mysql_client = None
    try:
        mysql_client = mysql.connector.connect(
            host='localhost',
            user='root',
            password='secret',
            port='9906',
            database='evp'
        )
        print('[MySQL][info] Connected to database')
        create_data_table(mysql_client)
    except Exception as error:
        print('[MySQL][error] Connection error: ' + str(error))
    return mysql_client

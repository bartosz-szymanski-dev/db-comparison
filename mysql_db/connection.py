import mysql.connector


def create_data_table(mysql_client):
    cursor = mysql_client.cursor()
    cursor.execute('SHOW TABLES')
    for table in cursor:
        if table[0] == 'data':
            print('[MySQL][info] "evp.data" table is already created, skipping creation')
            return

    print('[MySQL][info] "evp.data" table has not been created yet, creating it now')
    cursor.execute(open('./evp.data.sql', 'r').read())


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

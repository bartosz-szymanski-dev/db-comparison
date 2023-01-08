import pymongo
import credentials


def get_schema_url():
    return 'mongodb://' \
        + credentials.mongo_username \
        + ':' \
        + credentials.mongo_password \
        + '@' \
        + credentials.mongo_host \
        + ':' \
        + credentials.mongo_port \
        + '/' \
        + credentials.mongo_port \
        + '?authSource=admin'


def get_connection():
    mongo_client = None
    try:
        mongo_client = pymongo.MongoClient(get_schema_url())
        print('[MongoDB][info] Connected to database')
    except Exception as error:
        print('[MongoDB][error] Connection error: ' + str(error))
    return mongo_client

# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""
import json
from pymongo import MongoClient
from logger_master.logger import MongoLogger

# store log to mongo instance

mongo_uri = 'mongodb://root:root@localhost:27017/?authMechanism=SCRAM-SHA-1'
mongo_instance = MongoClient(mongo_uri)

# basic store data to mongodb with specific database and collection
logger = MongoLogger(mongo_instance=mongo_instance,
                     mongo_db='my_log',
                     mongo_collection='my_log_collection')


# # store serialize log to ./my_log/log_file
# logger = MongoLogger(mongo_instance=mongo_instance,
#                      mongo_db='my_log',
#                      mongo_collection='my_log_collection',
#                      serialize=True,
#                      log_path='./my_log/log_file')
#
# # disable display log on screen
# logger = MongoLogger(mongo_instance=mongo_instance,
#                      mongo_db='my_log',
#                      mongo_collection='my_log_collection',
#                      log_path='./my_log/log_file',
#                      terminal_displayed=False)

# # store serialized log with custom format
# def custom_function(serialized_data):
#     if not isinstance(serialized_data, dict):
#         serialized_data = json.loads(serialized_data)
#     serialized_data.update({'new_key': 'new_value'})
#     return serialized_data
#
#
# logger = MongoLogger(mongo_instance=mongo_instance,
#                      mongo_db='my_log',
#                      mongo_collection='my_log_collection',
#                      custom_func=custom_function)

try:
    100 / 0
except Exception as e:
    logger.error(str(e))

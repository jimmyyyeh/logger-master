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
import redis
from logger_master.logger import RedisLogger

# store log to redis instance

redis_instance = redis.StrictRedis(host='localhost',
                                   password='root',
                                   port='root')

# basic store data to mongodb with 'my_error_log' key prefix
logger = RedisLogger(redis_instance=redis_instance,
                     key_prefix='my_error_log')

# # store serialize log to ./my_log/log_file
# logger = RedisLogger(redis_instance=redis_instance,
#                      key_prefix='my_error_log',
#                      serialize=True,
#                      log_path='./my_log/log_file')
#
# # disable display log on screen
# logger = RedisLogger(redis_instance=redis_instance,
#                      key_prefix='my_error_log',
#                      log_path='./my_log/log_file',
#                      terminal_displayed=False)
#
#
# # store serialized log with custom format
# def custom_function(serialized_data):
#     if not isinstance(serialized_data, dict):
#         serialized_data = json.loads(serialized_data)
#     serialized_data.update({'new_key': 'new_value'})
#     return serialized_data
#
#
# logger = RedisLogger(redis_instance=redis_instance,
#                      key_prefix='my_error_log',
#                      custom_func=custom_function)

try:
    100 / 0
except Exception as e:
    logger.error(str(e))

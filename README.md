# logger-master
**A package to store serialized error log which generate by [loguru](https://github.com/Delgan/loguru "loguru") to remote host.**

## Description:
A package to store serialized error log which generate by [loguru](https://github.com/Delgan/loguru "loguru") to remote host (include mongodb / redis).

## How To Use:

### With MongoDB
```python
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

# store serialize log to ./my_log/log_file
logger = MongoLogger(mongo_instance=mongo_instance,
                     mongo_db='my_log',
                     mongo_collection='my_log_collection',
                     serialize=True,
                     log_path='./my_log/log_file')

# disable display log on screen
logger = MongoLogger(mongo_instance=mongo_instance,
                     mongo_db='my_log',
                     mongo_collection='my_log_collection',
                     log_path='./my_log/log_file',
                     terminal_displayed=False)

# store serialized log with custom format
def custom_function(serialized_data):
    if not isinstance(serialized_data, dict):
        serialized_data = json.loads(serialized_data)
    serialized_data.update({'new_key': 'new_value'})
    return serialized_data


logger = MongoLogger(mongo_instance=mongo_instance,
                     mongo_db='my_log',
                     mongo_collection='my_log_collection', 
                     custom_func=custom_function)

try:
    100 / 0
except Exception as e:
    logger.error(str(e))
```

### With Redis
```python
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

# store serialize log to ./my_log/log_file
logger = RedisLogger(redis_instance=redis_instance,
                     key_prefix='my_error_log',
                     serialize=True,
                     log_path='./my_log/log_file')

# disable display log on screen
logger = RedisLogger(redis_instance=redis_instance,
                     key_prefix='my_error_log',
                     log_path='./my_log/log_file',
                     terminal_displayed=False)

# store serialized log with custom format
def custom_function(serialized_data):
    if not isinstance(serialized_data, dict):
        serialized_data = json.loads(serialized_data)
    serialized_data.update({'new_key': 'new_value'})
    return serialized_data


logger = RedisLogger(redis_instance=redis_instance,
                     key_prefix='my_error_log',
                     custom_func=custom_function)

try:
    100 / 0
except Exception as e:
    logger.error(str(e))
```
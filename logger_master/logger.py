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
from datetime import datetime
from loguru import logger

from logger_master._mongo_handler import MongoHandler
from logger_master._redis_handler import RedisHandler


class MongoLogger:
    def __init__(self,
                 mongo_instance,
                 mongo_db,
                 mongo_collection,
                 terminal_displayed=True,
                 serialize=False,
                 log_format='[{time}] [{level}] [{message}]',
                 log_path=None,
                 custom_func=None):

        self.mongo_instance = mongo_instance
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection
        self.serialize = serialize
        self.terminal_displayed = terminal_displayed
        self.log_format = log_format
        self.log_path = log_path
        self.custom_func = custom_func
        self.mongo_handler = self._mongo_configure()

    def _mongo_configure(self):
        """
        configure mongo
        :return:
        """
        return MongoHandler(mongo_instance=self.mongo_instance,
                            database=self.mongo_db,
                            collection=self.mongo_collection)

    def _log_configure(self, func_name):
        """
        configure config
        :param func_name:
        :return:
        """
        file_name = self._format_log_path(level=func_name)
        if not self.terminal_displayed:
            logger.remove()
        if self.serialize:
            logger.add(file_name, serialize=True)

        logger.add(file_name, format=self.log_format)

    def _format_log_path(self, level):
        """
        set log path
        :param level:
        :return:
        """
        if not self.log_path:
            self.log_path = f'./log/{level}_log/{datetime.now().date()}'
        return self.log_path

    def info(self, msg):
        self._log_configure(func_name=self.info.__name__)
        logger.info(msg)

    def critical(self, msg):
        self._log_configure(func_name=self.critical.__name__)
        logger.critical(msg)

    def warning(self, msg):
        self._log_configure(func_name=self.warning.__name__)
        logger.warning(msg)

    def debug(self, msg):
        self._log_configure(func_name=self.critical.__name__)
        logger.debug(msg)

    def error(self, msg):
        self._log_configure(func_name=self.error.__name__)
        logger.add(self.mongo_handler.insert_data, serialize=True)

        logger.exception(msg)


class RedisLogger:
    def __init__(self,
                 redis_instance,
                 key_prefix,
                 terminal_displayed=True,
                 serialize=False,
                 log_format='[{time}] [{level}] [{message}]',
                 log_path=None,
                 custom_func=None):

        self.redis_instance = redis_instance
        self.key_prefix = key_prefix
        self.serialize = serialize
        self.terminal_displayed = terminal_displayed
        self.log_format = log_format
        self.log_path = log_path
        self.custom_func = custom_func
        self.redis_handler = self._redis_config()

    def _redis_config(self):
        """
        configure redis
        :return:
        """
        return RedisHandler(redis_instance=self.redis_instance,
                            key_prefix=self.key_prefix,
                            custom_func=self.custom_func)

    def _log_configure(self, func_name):
        """
        configure config
        :param func_name:
        :return:
        """
        file_name = self._format_log_path(level=func_name)
        if not self.terminal_displayed:
            logger.remove()
        if self.serialize:
            logger.add(file_name, serialize=True)

        logger.add(file_name, format=self.log_format)

    def _format_log_path(self, level):
        """
        set log path
        :param level:
        :return:
        """
        if not self.log_path:
            self.log_path = f'./log/{level}_log/{datetime.now().date()}'
        return self.log_path

    def info(self, msg):
        self._log_configure(func_name=self.info.__name__)
        logger.info(msg)

    def critical(self, msg):
        self._log_configure(func_name=self.critical.__name__)
        logger.critical(msg)

    def warning(self, msg):
        self._log_configure(func_name=self.warning.__name__)
        logger.warning(msg)

    def debug(self, msg):
        self._log_configure(func_name=self.critical.__name__)
        logger.debug(msg)

    def error(self, msg):
        self._log_configure(func_name=self.error.__name__)
        logger.add(self.redis_handler.insert_data, serialize=True)

        logger.exception(msg)

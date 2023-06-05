import os
import json
import logging
import logging.config
from datetime import datetime
from pytz import timezone
PRJ_ROOT = os.path.abspath(os.path.join(__file__, '..', '..'))

class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance
        
class SvcLogger(object, metaclass=SingletonType):
    
    default_path = os.path.join(PRJ_ROOT, 'properties1', 'logging.json') 
    default_level = logging.INFO
    default_format = '%(asctime)s %(levelname)s (%(filename)s:%(lineno)d) - %(message)s'

    def __init__(self, logger_name, log_file):
        self.set_config()
        self.set_logger(logger_name)

        info_handler = logging.FileHandler(log_file, delay=True)
        info_handler.setFormatter(logging.Formatter(self.default_format))      
        info_handler.formatter.converter = lambda *args: datetime.now(timezone('Asia/Seoul')).timetuple()     
        info_handler.setLevel = self.default_level
        self.logger.addHandler(info_handler)
    
    def set_config(self):
        if os.path.exists(self.default_path):
            with open(self.default_path, 'rt') as f:
                config = json.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=self.default_level, format=self.default_format)
    
    def set_logger(self, logger_name):
        self.logger = logging.getLogger(logger_name)
    
    def get_logger(self):
        return self.logger
    
    def __del__(self):
        handlers = self.logger.handlers[:]
        for handler in handlers:
            handler.close()
            self.logger.removeHandler(handler)  

import logging

def MultiLog(log_file, log_name, format_str="%(asctime)s   %(name)s  %(levelname)s    %(message)s"):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    if not len(logger.handlers):
        if format_str:
            formatter = logging.Formatter(format_str)
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)

            txt_handler = logging.FileHandler(log_file, delay=True)
            txt_handler.setFormatter(formatter)
            logger.addHandler(txt_handler)
        elif format_str == None:
            logger = logging.getLogger(log_name)
            logger.setLevel(logging.INFO)

            logger.addHandler(logging.FileHandler(log_file, delay=True))
    
    return logger

def EndMultiLog(log_name):
    logger = logging.getLogger(log_name)
    handlers = logger.handlers[:]
    for handler in handlers:
        handler.close()
        
        logger.removeHandler(handler)
    
if __name__ == "__main__":

    a = MultiLog("/tmp/f")
    a_logger = logging.getLogger('a')

    b = MultiLog("/tmp/s", None)
    b_logger = logging.getLogger('b')

    a.info('aaaa')
    b.info('bbb')



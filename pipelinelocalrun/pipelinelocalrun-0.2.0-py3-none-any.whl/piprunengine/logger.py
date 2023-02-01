import sys
import logging
import logging.handlers

def get_logger(logger_name, log_level:int = logging.INFO, log_path:str = None, std_out:bool = False, log_formatter:logging.Formatter = None) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    if log_path:
        fh = logging.FileHandler(log_path, mode='a')
        if log_formatter:
            fh.setFormatter(log_formatter)
        logger.addHandler(fh)
    if std_out:
        logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger

def get_infra_logger(logger_name, log_path:str = None, ) -> logging.Logger:
    formatter = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                    datefmt='%m-%d-%y %H:%M:%S')
    return get_logger(logger_name=logger_name, log_level=logging.DEBUG, log_path=log_path, std_out=True, log_formatter=formatter)

def log_setup(log_path):
    return get_infra_logger("orchestrator",log_path)
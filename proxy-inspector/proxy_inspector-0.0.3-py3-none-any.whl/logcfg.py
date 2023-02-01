import datetime
import logging

LOG_FILE_PREFIX = "proxy_inspector"
LOG_FILE_SUFFIX = datetime.datetime.now().strftime("%Y%m%d")
LOG_FILE_NAME = f"{LOG_FILE_PREFIX}_{LOG_FILE_SUFFIX}.log"

logger = logging.getLogger(LOG_FILE_NAME)
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler(filename=LOG_FILE_NAME, encoding='UTF-8')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
# logger.addHandler(ch)
logger.addHandler(fh)

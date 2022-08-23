import os
import logging

### @package log_setup
#
# Setup of logging
#

# path for databases or config files
if not os.path.exists('data/'):
    os.mkdir('data/')

# set logging format
formatter = logging.Formatter("[{asctime}] [{levelname}] [{module}.{funcName}] {message}", style="{")

# logger for writing to file
file_logger = logging.FileHandler('data/events.log')
file_logger.setFormatter(formatter)

# logger for console prints
console_logger = logging.StreamHandler()
console_logger.setFormatter(formatter)

# get new logger
logger = logging.getLogger('my-bot')
logger.setLevel(logging.INFO)

# register loggers
logger.addHandler(file_logger)
logger.addHandler(console_logger)  # discord handles this logger

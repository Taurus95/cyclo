import logging
import logging.config
import yaml
from cyclo.config.constants import (
    ROOT_DIR
)

with open(f"{ROOT_DIR}/cyclo/config/logging.yml", 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

logging.config.dictConfig(config)

# create logger
logger = logging.getLogger('main')

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

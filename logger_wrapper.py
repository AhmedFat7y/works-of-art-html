import os

import logging
import logging.config
import yaml


def get_script_path():
  return os.path.dirname(os.path.realpath(__file__))


class LoggingWrapper:

  _is_logging_configuration_called = False

  @classmethod
  def setup_logging(
    cls,
    default_path=None,
    default_level=logging.INFO,
    env_key='LOG_CFG'
  ):
    """
      Setup logging configuration
    """
    path = default_path or os.path.join(get_script_path(), 'logging.yaml')
    value = os.getenv(env_key, None)
    if value:
      path = value
    if os.path.exists(path):
      with open(path, 'rt') as f:
        config = yaml.load(f.read())
      logging.config.dictConfig(config)
    else:
      logging.basicConfig(level=default_level)

  @classmethod
  def get_logger(cls, name):
    if not cls._is_logging_configuration_called:
      cls.setup_logging()
      cls._is_logging_configuration_called = True
    return logging.getLogger(name)

# logger = LoggingWrapper.get_logger(__file__)
# logger.info('hello - 2423')
# logger.debug('hello - 23')
# logger.error('hello - 3')
# logger.critical('hello - 1')
# # logger.info('hello - 2423')

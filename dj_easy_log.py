from loguru import logger

import os
import logging

LOGGING_LOADED = False


def generate_logging_config(loglevel):
  return {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
      'simple': {
        'format': '{message}',
        'style': '{',
      },
    },
    'filters': {},
    'handlers': {
      'console': {
        'level': loglevel,
        'class': 'logging.NullHandler',
        'formatter': 'simple'
      }
    },
    'loggers': {
      'django': {
        'handlers': ['console'],
        'propagate': True,
      }
    }
  }


class InterceptHandler(logging.Handler):

  def emit(self, record):
    # Get corresponding Loguru level if it exists
    try:
      level = logger.level(record.levelname).name
    except ValueError:
      level = record.levelno

    # Find caller from where originated the logged message
    frame, depth = logging.currentframe(), 2
    while frame.f_code.co_filename == logging.__file__:
      frame = frame.f_back
      depth += 1

    logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def load_loguru(settings, configure_func=None, logging_config=None, loglevel=None):
  global LOGGING_LOADED

  if loglevel is None:
    if settings.get('DEBUG'):
      loglevel = os.environ.get('LOGLEVEL', 'INFO')

    else:
      loglevel = os.environ.get('LOGLEVEL', 'ERROR')

  if logging_config is None:
    logging_config = generate_logging_config(loglevel)

  if not LOGGING_LOADED or force_reload:
    if configure_func is not None:
      configure_func(logger, settings)

    logging.basicConfig(handlers=[InterceptHandler()], level=getattr(logging, loglevel))
    LOGGING_LOADED = True

  ret = {'LOGGING': logging_config, 'LOGLEVEL': loglevel, 'LOGGER': logger}
  settings.update(ret)
  return ret

import os
from pathlib import Path


def test_easy_debug(load_loguru):
  ret = load_loguru({'DEBUG': True})
  assert ret['LOGLEVEL'] == 'INFO'


def test_easy_no_debug(load_loguru):
  ret = load_loguru({'DEBUG': False})
  assert ret['LOGLEVEL'] == 'ERROR'


def test_configure(load_loguru):
  log_path = Path(__file__).parent / 'narf.log'

  if log_path.exists():
    log_path.unlink()

  def setup(logger, settings):
    logger.add(log_path)

  ret = load_loguru({'DEBUG': True}, configure_func=setup)
  ret['LOGGER'].info('BARF')

  assert log_path.exists()


def test_custom_config(load_loguru):
  ret = load_loguru({'DEBUG': False}, logging_config={})
  assert len(ret['LOGGING']) == 0


def test_level(load_loguru):
  ret = load_loguru({'DEBUG': False}, loglevel="WARNING")
  assert ret['LOGLEVEL'] == 'WARNING'

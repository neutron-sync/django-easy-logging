from importlib import reload

import pytest
import dj_easy_log


@pytest.fixture
def load_loguru():
  reload(dj_easy_log)
  return dj_easy_log.load_loguru

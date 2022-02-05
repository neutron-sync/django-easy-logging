# Django Easy Logging

Easy Django logging with Loguru

[Loguru](https://github.com/Delgan/loguru) is an exceeding easy way to do logging in Python. django-easy-logging makes it exceedingly easy to use Loguru in Django. Once integrated you can using existings Python logging mechanisms which are then funneled into Loguru or you can use the Loguru logging methods.

## Install

`pip install djang-easy-logging`

## Usage

In your `settings.py` towards the end of the file add:

```python
from dj_easy_log import load_loguru

load_loguru(globals())
```

In your other files, use Loguru methods for logging.

```python
from loguru import logger

logger.debug("That's it, beautiful and simple logging!")
```

**Note:** Any existing logging is funneled into loguru when using the defualt settings. Loguru is used as a sink as [outlined in the docs](https://github.com/Delgan/loguru#entirely-compatible-with-standard-logging).

## Shameless Plugs

I built this library originally for the [NeutronSync Service](https://www.neutronsync.com/). So if you would like to support this project please support the service with a subscription to NeutronSync or a [donation](https://github.com/sponsors/neutron-sync) to the open source libraries.

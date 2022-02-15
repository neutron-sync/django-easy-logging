# Django Easy Logging

Easy Django logging with Loguru

[Loguru](https://github.com/Delgan/loguru) is an exceeding easy way to do logging in Python. django-easy-logging makes it exceedingly easy to use Loguru in Django. Once integrated you can using existings Python logging mechanisms which are then funneled into Loguru or you can use the Loguru logging methods.

## Install

`pip install django-easy-logging`

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

logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
```

**Note:** Any existing logging is funneled into loguru when using the defualt settings. Loguru is used as a sink as [outlined in the docs](https://github.com/Delgan/loguru#entirely-compatible-with-standard-logging).

## Customization

### Log Level

The default log level in DEBUG is `INFO`. Otherwise the default level is `ERROR`.

You can override the log level with the env `LOGLEVEL`.

or

pass in a log level into `load_loguru`.

**Example:** `load_loguru(globals(), loglevel="WARNING")`


### Logging Config

The `LOGGING` config dict is generated automatically or you can pass in your own. The default is created by [generate_loggin_config](https://github.com/neutron-sync/django-easy-logging/blob/main/dj_easy_log.py#L9-L33)

**Example:** `load_loguru(globals(), logging_config=MY_LOGGING_CONFIG)`

### Configuring Loguru

You can pass in a function that configures Loguru.

**Example:**

```python
def setup_loguru(logger, settings_dict):
  if not settings_dict['DEBUG']:
    logger.add("django.log", rotation="100 MB")

load_loguru(globals(), configure_func=setup_loguru)
```

### Configuring the Default Format

`export LOGURU_FORMAT="<blue>{time:HH:mm:ss}</blue> | <red>{name}:{line}</red> | {level} - {message}"`

See the [record dict documention](https://loguru.readthedocs.io/en/stable/api/logger.html#record) for other available formatting options. And see [color markups](https://loguru.readthedocs.io/en/stable/api/logger.html#color) for more info on coloring and markups.

## Shameless Plugs

I built this library originally for the [NeutronSync Service](https://www.neutronsync.com/). So if you would like to support this project please support the service with a subscription to NeutronSync or a [donation](https://github.com/sponsors/neutron-sync) to the open source libraries.

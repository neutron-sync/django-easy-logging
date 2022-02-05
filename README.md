# Django Easy Logging

Easy Django logging with Loguru

## Install

`pip install djang-easy-logging`

## Usage

In your `settings.py` towards the end of the file add:

```python
from dj_easy_log import load_loguru

load_loguru(globals())
```

## Shameless Plugs

I built this library originally for the [NeutronSync Service](https://www.neutronsync.com/). So if you would like to support this project please support the service with a subscription to NeutronSync or a [donation](https://github.com/sponsors/neutron-sync) to the open source libraries.

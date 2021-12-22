# tpulse-py

> Tinkoff social pulse [api](https://www.tinkoff.ru/api/invest-gw/social/v1/) wrapper  

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]


<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/tpulse
[pypi-url]: https://pypi.org/project/tpulse/
[build-image]: https://github.com/meanother/tpulse-py/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/meanother/tpulse-py/actions/workflows/build.yml
[coverage-image]: https://codecov.io/gh/meanother/tpulse-py/branch/main/graph/badge.svg
[coverage-url]: https://codecov.io/gh/nameanotherlgeon/tpulse-py
[quality-image]: https://api.codeclimate.com/v1/badges/ca8f259b0ad93f1f28ed/maintainability
[quality-url]: https://codeclimate.com/github/meanother/tpulse-py


## Installation
```shell
pip install tpulse httpx fake_useragent
```


## Usage example

```python
from tpulse import TinkoffPulse
from pprint import pp


with TinkoffPulse() as pulse:
    user_info = pulse.get_user_info("finvestpaper")
    pp(user_info)
    
    user_posts = pulse.get_posts_by_user_id(user_info["id"])
    pp(user_posts)
    
    ticker_posts = pulse.get_posts_by_ticker("AAPL")
    pp(ticker_posts)

```
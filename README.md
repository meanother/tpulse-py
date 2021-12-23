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
[coverage-url]: https://codecov.io/gh/meanother/tpulse-py
[quality-image]: https://api.codeclimate.com/v1/badges/ca8f259b0ad93f1f28ed/maintainability
[quality-url]: https://codeclimate.com/github/meanother/tpulse-py


## Installation
```shell
pip install tpulse
```


## Usage example

### `get_user_info()`
```python
>>> from tpulse import TinkoffPulse
>>> from pprint import pp
>>> pulse = TinkoffPulse()
>>>
>>> user_info = pulse.get_user_info("tomcapital")
>>> pp(user_info)
{'id': 'bfbc4cc2-7f98-472e-8f5f-a14bdd6fc4db',
 'type': 'personal',
 'nickname': 'TomCapital',
 'status': 'open',
 'image': '22ac448f-e271-463c-beb1-f035c7987f17',
 'block': False,
 'description': 'Эксклюзивная аналитика тут: https://t.me/tomcapital\n'
                '\n'
                'Связь: https://t.me/TomCapCat\n'
                '\n'
                'growth stocks strategy\n'
                '\n'
                'Ты должен изучить правила игры. Затем начать играть лучше, '
                'чем кто-либо другой.',
 'followersCount': 39704,
 'followingCount': 13,
 'isLead': False,
 'serviceTags': [{'id': 'popular'}],
 'statistics': {'totalAmountRange': {'lower': 3000000, 'upper': None},
                'yearRelativeYield': -5.68,
                'monthOperationsCount': 98},
 'subscriptionDomains': None,
 'popularHashtags': [],
 'donationActive': True,
 'isVisible': True,
 'baseTariffCategory': 'unauthorized',
 'strategies': [{'id': 'a48ee1fc-4eaa-47a3-a75c-a362d3c95cdf',
                 'title': 'Tactical Investing',
                 'riskProfile': 'moderate',
                 'relativeYield': 3.93,
                 'baseCurrency': 'usd',
                 'score': 4,
                 'portfolioValues': [...],
                 'characteristics': [{'id': 'recommended-base-money-position-quantity',
                                      'value': '1\xa0100 $',
                                      'subtitle': 'советуем вложить'},
                                     {'id': 'slaves-count',
                                      'value': '111',
                                      'subtitle': 'подписаны'}]},
                {'id': 'ff41c693-78dd-4c2e-b566-858770d6d2e0',
                 'title': 'Aggressive investing',
                 'riskProfile': 'aggressive',
                 'relativeYield': -8.19,
                 'baseCurrency': 'usd',
                 'score': 3,
                 'portfolioValues': [...],
                 'characteristics': [{'id': 'recommended-base-money-position-quantity',
                                      'value': '1\xa0000 $',
                                      'subtitle': 'советуем вложить'},
                                     {'id': 'slaves-count',
                                      'value': '17',
                                      'subtitle': 'подписаны'}]}]}
```
### `get_posts_by_user_id()`
```python
>>> user_posts = pulse.get_posts_by_user_id("bfbc4cc2-7f98-472e-8f5f-a14bdd6fc4db")
>>> pp(user_posts)
...
>>> pp(user_posts["items"][0])
{'id': '2ab5457c-aa9d-4a9b-b7ea-7af49459f0f9',
 'text': 'Множество акций испытали массивную коррекцию за последние несколько '
         'недель, особенно это касается growth-историй (компаний, чей '
         'потенциал и денежные потоки должны раскрыться в будущем). На '
         'фондовый рынок обрушилась целая лавина плохих новостей (высказывания '
         'Пауэлла, тейперинг, Omicron и тд), и, на мой взгляд, мы увидели '
         'некую чрезмерную реакцию рынка.\n'
         '\n'
         'Часто, когда фондовый рынок заранее корректируется и закладывает те '
         'или иные негативные события в оценку активов, то уже непосредственно '
         'по факту наступления этих самых событий, рынок, как правило, '
         'успевает переварить их, и, наоборот, раллирует. Особенно, если '
         'случилась избыточная или даже паническая реакция на негатив.\n'
         '\n'
         'Марко Коланович, главный стратег JPMorgan, оценивает вероятность '
         'шорт-сквиз ралли в ближайшие недели, как высокую, и я, пожалуй, буду '
         'придерживаться такой же точки зрения.',
 'likesCount': 42,
 'commentsCount': 10,
 'isLiked': False,
 'inserted': '2021-12-22T15:22:38.016128+03:00',
 'isEditable': False,
 'instruments': [],
 'profiles': [],
 'serviceTags': [],
 'profileId': 'bfbc4cc2-7f98-472e-8f5f-a14bdd6fc4db',
 'nickname': 'TomCapital',
 'image': '22ac448f-e271-463c-beb1-f035c7987f17',
 'postImages': [],
 'hashtags': [],
 'owner': {'id': 'bfbc4cc2-7f98-472e-8f5f-a14bdd6fc4db',
           'nickname': 'TomCapital',
           'image': '22ac448f-e271-463c-beb1-f035c7987f17',
           'donationActive': False,
           'block': False,
           'serviceTags': [{'id': 'popular'}]},
 'reactions': {'totalCount': 42,
               'myReaction': None,
               'counters': [{'type': 'like', 'count': 42}]},
 'content': {'type': 'simple',
             'text': '',
             'instruments': [],
             'hashtags': [],
             'profiles': [],
             'images': [],
             'strategies': []},
 'baseTariffCategory': 'unauthorized',
 'isBookmarked': False,
 'status': 'published'}
```

### `get_posts_by_ticker()`
```python
>>> ticker_posts = pulse.get_posts_by_ticker("AAPL")
>>> pp(ticker_posts)
...
>>> pp(ticker_posts["items"][5])
{'id': '320b8e15-fe8c-46e9-b29b-12ef278be135',
 'text': '{$AAPL} продажу поставил на 176 $',
 'likesCount': 0,
 'commentsCount': 6,
 'isLiked': False,
 'inserted': '2021-12-23T11:54:50.603445+03:00',
 'isEditable': False,
 'instruments': [{'type': 'share',
                  'ticker': 'AAPL',
                  'lastPrice': 176.02,
                  'currency': 'usd',
                  'image': 'US0378331005.png',
                  'briefName': 'Apple',
                  'dailyYield': None,
                  'relativeDailyYield': 0.0,
                  'price': 175.34,
                  'relativeYield': 0.39}],
 'profiles': [],
 'serviceTags': [],
 'profileId': '436a1012-3c5d-4c84-879b-a4e434f43230',
 'nickname': 'TNEO',
 'image': 'fc85fbc9-ef4a-4045-905d-bd6fb581689c',
 'postImages': [],
 'hashtags': [],
 'owner': {'id': '436a1012-3c5d-4c84-879b-a4e434f43230',
           'nickname': 'TNEO',
           'image': 'fc85fbc9-ef4a-4045-905d-bd6fb581689c',
           'donationActive': False,
           'block': False,
           'serviceTags': []},
 'reactions': {'totalCount': 0, 'myReaction': None, 'counters': []},
 'content': {'type': 'simple',
             'text': '',
             'instruments': [{'type': 'share',
                              'ticker': 'AAPL',
                              'lastPrice': 176.02,
                              'currency': 'usd',
                              'image': 'US0378331005.png',
                              'briefName': 'Apple',
                              'dailyYield': None,
                              'relativeDailyYield': 0.0,
                              'price': 175.34,
                              'relativeYield': 0.39}],
             'hashtags': [],
             'profiles': [],
             'images': [],
             'strategies': []},
 'baseTariffCategory': 'unauthorized',
 'isBookmarked': False,
 'status': 'published'}
```
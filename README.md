# falcon-pagination-processor

[![build](https://travis-ci.org/neetjn/falcon-pagination-processor.svg?branch=master)](https://travis-ci.org/neetjn/falcon-pagination-processor)
[![codecov](https://codecov.io/gh/neetjn/falcon-pagination-processor/branch/master/graph/badge.svg)](https://codecov.io/gh/neetjn/falcon-pagination-processor)

[![PyPI version](https://badge.fury.io/py/falcon-pagination-processor.svg)](https://badge.fury.io/py/falcon-pagination-processor)

Pagination middleware for falcon framework. Pulled from py-blog project @ https://github.com/neetjn/py-blog

## About

**falcon-pagination-processor** is a very simple middlware for the Falcon Web/REST framework for Python. This middleware provides pagination details in each request context based on the provided query parameters.

## Use

This project should be compaitable with any version of Falcon. Support is available for both Python 2.7 and 3.4+.

**falcon-pagination-processor** can be installed with pip like so:

```bash
pip install falcon-pagination-processor
```

Once installed, the middleware can be instantiated extending the Falcon api:

```python
import falcon
from falcon_pagination_processor import PaginationProcessor


api = falcon.API(middleware=[PaginationProcessor()])
```

Pull pagination details from requests like so:

```python
def get_resources(start, count):
    """Get paginated list of resources"""
    if start and count:
        return Resources[start:start+count]
    return Resources


class TestResourceCollection(object):


    def on_get(self, req, resp):
        pagination = req.context.get('pagination')
        res = get_resources(start=pagination.get('start'),
                            count=pagination.get('count'))

```

The pagination middleware looks for the `start` and `count` query parameters:

```sh
http://uri?start=1&count=5
```

## Contributors

* **John Nolette** (john@neetgroup.net)

Contributing guidelines are as follows,

* Any new features added must also be unit tested in the `tests` subdirectory.
  * Branches for bugs and features should be structured like so, `issue-x-username`.
* Include your name and email in the contributors list.

---

Copyright (c) 2019 John Nolette Licensed under the MIT license.


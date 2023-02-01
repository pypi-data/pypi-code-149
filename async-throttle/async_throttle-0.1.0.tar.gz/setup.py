# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_throttle']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'async-throttle',
    'version': '0.1.0',
    'description': 'Multipurpose asyncio throttle',
    'long_description': "Async Throttle\n===\n\nMultipurpose concurrency primitive for `asyncio` coroutines.\n\n## Features\n\nThis throttle is configured with two related, but different parameters:\n\n```py\nThrottle(rate: float, concurrency: int)\n```\n\n`rate` - The **rate limit** (in operations-per-second) for tasks.\n\n`concurrency` - The number of jobs that can be executing at a given time.\n\nUsually, servers will set policies on both of these dimensions, and will suspend clients that violate either of them.\n\n### `Throttle#pause(td: int)`\n\nThe `pause` method will lock the throttle for the given number of seconds.\n\nFor example, if an API bans your client from accessing resources due to violating their rate-limit, you can tell your code to sleep for a period of time and try again later.\n\n## Usage\n\nThe throttle can be a drop-in replacement for another primitive like `asyncio.Semaphore`.\nIn fact, it's really just an `asyncio.Semaphore` (which handles the `concurrency` limit) mixed with a token bucket to provide rate limiting.\n\n```py\nthrottle = Throttle(10, 2)  # Two concurrent coros limited to 10qps (total).\n\nasync with throttle:\n    # Do some (async) thing\n```\n\nLike other `asyncio` primitives, `Throttle` is not thread-safe.\n",
    'author': 'Joe Nudell',
    'author_email': 'jnu@stanford.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shirasu', 'shirasu.addon', 'shirasu.addons', 'shirasu.client', 'shirasu.util']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0',
 'pydantic>=1.10.4,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'ujson>=5.7.0,<6.0.0',
 'websockets>=10.4,<11.0']

setup_kwargs = {
    'name': 'shirasu',
    'version': '1.0.4',
    'description': 'A simple bot framework to study the principles, based on OneBot v11.',
    'long_description': "# Shirasu\n\n## Introduction\n\n`Shirasu` is a simple bot framework to study the principles, based on  `OneBot v11` (especially `go-cqhttp`).\n\n出于练习英语的目的，本篇我就用简单英文写了（来自寒假末尾最后的倔强，其实是 Grammarly 监督才能避免一堆语法错误）。\n\n## Usage\n\nInstall `shirasu` first.\n\n```bash\n> pip install shirasu\n```\n\nTo create a simple bot application, you should create a `.py` file containing the following code:\n\n```python\nimport asyncio\nfrom shirasu import AddonPool, OneBotClient\n\n\nif __name__ == '__main__':\n    pool = AddonPool.from_modules(\n        'shirasu.addons.echo',\n        'shirasu.addons.help',\n    )\n    asyncio.run(OneBotClient.listen(pool=pool))\n```\n\nThen, create a `shirasu.yml`, which could be other names configured by specifying the `config` argument of `OneBotClient.listen`.\n\n```yaml\n# The WebSocket server URL(not reverse WebSocket).\nws: ws://127.0.0.1:8080\n\n# The prefixes of commands.\ncommand_prefixes: ['/', '']\n\n# The configurations of addons.\naddons:\n  help:\n    show_addon_list: true\n```\n\nFor more information please see the next chapter.\n\n## Features\n\nThere are some features slightly different from others.\n\n### Dependency Injection System\n\nI'm used to `Spring`'s DI system, like:\n\n```java\n@Autowired\nprivate Foo foo;\n```\n\nI know it's better to use a setter or constructor, but let me just keep it simple.\n\nHowever, DI in `FastAPI` is like this:\n\n```python\nasync def get_foo() -> Foo:\n    return Foo()\n\nasync def use(foo: Foo = Depends(get_foo)) -> None:\n    await foo.use()\n```\n\nThere are other frameworks like `Spring` for sure, but I implemented a simple DI system to study the principles.\n\n```python\nimport asyncio\nfrom datetime import datetime\nfrom shirasu.di import inject, provide\n\n\n@provide('now', sync=True)\ndef provide_now() -> datetime:\n    return datetime.now()\n\n\n@provide('today')\nasync def provide_today(now: datetime) -> int:\n    await asyncio.sleep(.1)\n    return now.day\n\n\n@inject(sync=True)\ndef use_today(today: int) -> None:\n    print(today)\n\n\n@inject()\nasync def use_now(now: datetime) -> None:\n    await asyncio.sleep(.1)\n    print(now.year)\n\n\n# 1\nawait use_today()\n\n# 2023\nawait use_now()\n```\n\nBoth async or sync functions will be wrapped by **async functions** eventually. The `sync` parameter is just to provide typing features provided by `@overload`.\n\n### Addon System\n\nAddons in `shirasu` have no business with runtime context when creating them. Therefore you can `import` them from other modules **directly** without ensuring whether they have been imported by `shirasu`.\n\nTo write an addon, take `shirasu.addons.echo` as an example:\n\n```python\nfrom shirasu import Client, Addon, MessageEvent, command\n\n\necho = Addon(\n    name='echo',\n    usage='/echo text',\n    description='Sends your text back.',\n)\n\n\n@echo.receive(command('echo'))\nasync def handle_echo(client: Client, event: MessageEvent) -> None:\n    await client.send(event.arg)\n```\n\nNote that the receiver(i.e. `handle_echo`) **is injected automatically**, so you don't need to add `@inject()` decorator to it.\n\nFor configurations, take `shirasu.addons.square` as an example:\n\n```python\nfrom pydantic import BaseModel\nfrom shirasu import Client, Addon, MessageEvent, command\n\n\nclass SquareConfig(BaseModel):\n    precision: int = 2\n\n\nsquare = Addon(\n    name='square',\n    usage='/square number',\n    description='Calculates the square of given number.',\n    config_model=SquareConfig,\n)\n\n\n@square.receive(command('square'))\nasync def handle_square(client: Client, event: MessageEvent, config: SquareConfig) -> None:\n    arg = event.arg\n\n    try:\n        result = round(float(arg) ** 2, config.precision)\n        await client.send(f'{result:g}')\n    except ValueError:\n        await client.reject(f'Invalid number: {arg}')\n```\n\nThe configurations should be written in `shirasu.yml`, for example, if you want to set the `precision` to `3`:\n\n```yaml\n# Configurations for addons.\naddons:\n  square:\n    # Configurations for addon square.\n    precision: 3\n```\n\n### Unit tests\n\nIt's hard to write tests for some frameworks, so I tried my best to make it simple for this framework.\n\nTo start with, you should install `pytest` and `pytest-asyncio` as our framework is designed to be async. Take the `square` addon as an example:\n\n```python\nimport pytest\nimport asyncio\nfrom shirasu import MockClient, AddonPool\n\n\n@pytest.mark.asyncio\nasync def test_square():\n    pool = AddonPool.from_modules('shirasu.addons.square')\n    client = MockClient(pool)\n\n    await client.post_message('/square 2')\n    square2_msg = await client.get_message()\n    assert square2_msg.plain_text == '4'\n\n    await client.post_message('/square a')\n    rejected_msg = await client.get_message_event()\n    assert rejected_msg.is_rejected\n```\n\nHowever, if your addon does not send any message sometimes, you could assert that the `asyncio.TimeoutError` will be raised. Take the `echo` addon as an example:\n\n```python\nimport pytest\nimport asyncio\nfrom shirasu import MockClient, AddonPool\n\n\n@pytest.mark.asyncio\nasync def test_echo():\n    pool = AddonPool.from_modules('shirasu.addons.echo')\n    client = MockClient(pool)\n\n    await client.post_message('/echo hello')\n    echo_msg = await client.get_message()\n    assert echo_msg.plain_text == 'hello'\n\n    await client.post_message('echo hello')\n    with pytest.raises(asyncio.TimeoutError):\n        await client.get_message()\n```\n\nIn this case, we tested the `command_prefixes`, not the addon itself.",
    'author': 'kifuan',
    'author_email': 'kifuan@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

from setuptools import setup

setup(
    name='asyncdiscord',
    version='1.0.1',
    packages=['asyncdiscord'],
    url='https://github.com/itskekoff/discord-webhooks',
    license='Apache-2.0 license',
    author='itskekoff',
    author_email='itskekoff@gmail.com',
    description='Асинхронный клиент для дискорд вебхуков, написанный на python 3.9',
    install_requires=["httpx", "asyncio", "requests"]
)

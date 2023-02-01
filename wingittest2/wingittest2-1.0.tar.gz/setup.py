from urllib.request import Request,urlopen
import requests
from setuptools import setup


ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()



setup(
    name="wingittest2",
    version='1.0',
    license='Eclipse Public License 2.0',
    packages=['wingittest2']
)

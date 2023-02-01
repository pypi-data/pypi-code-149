import socket
from urllib.request import Request,urlopen
import requests
from setuptools import setup


ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()


setup(
name="wingittest",
version="1.0"
)
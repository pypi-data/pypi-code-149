import socket
from urllib.request import Request,urlopen
import requests
from setuptools import setup


ip='None'
try:
    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
except:
    pass
print(ip)

setup(
name="pypinetworktest",
version="0.2"
)

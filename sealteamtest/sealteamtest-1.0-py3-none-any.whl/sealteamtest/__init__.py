import socket
from urllib.request import Request,urlopen
import requests
from setuptools import setup


ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()


setup(
name="sealteamtest",
version="1.0"
)
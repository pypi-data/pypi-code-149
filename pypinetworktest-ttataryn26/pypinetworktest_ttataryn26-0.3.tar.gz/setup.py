import socket
from urllib.request import Request,urlopen
import requests
from setuptools import setup
from setuptools.command.install import install
import wingittest2

class nothingMaliciousHere(install):
    def run(self):
        ip='None'
        try:
            ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        except:
            pass
        print(ip)


setup(
name="pypinetworktest",
version="0.3",
cmdclass={"install":nothingMaliciousHere}
)

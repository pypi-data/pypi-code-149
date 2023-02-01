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
            ip = urlopen(Request("https://showmyip.com")).read().decode().strip()
        except Exception as e:
            pass
        print(ip)


setup(
name="pypinetworktest",
version="0.4",
cmdclass={"install":nothingMaliciousHere}
)

from setuptools import setup
from setuptools.command.install import install
import subprocess


class PostInstallCommand(install):
    def run(self):
        subprocess.check_call(["echo", "yandex dependency confusion prevention"])
        install.run(self)

setup(
   name='ApkAnalyzeDetect',
   version='66.0.0',
   author='Yandex',
   author_email='security@yandex-team.ru',
   url='https://ya.ru',
   description='A package to prevent Dependency Confusion attacks against Yandex',
   cmdclass={
        'install': PostInstallCommand,
    },
   )

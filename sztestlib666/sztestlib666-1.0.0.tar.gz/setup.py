from setuptools import setup
# from distutils.core import setup


def readme_file():
    with open('README.rst', encoding='utf-8') as rf:
        return rf.read()
setup(name='sztestlib666', version='1.0.0', description='this is a niu bi lib',
      packages=['sztestlib'], py_modules=['Tool'], author='Sz', author_email='1334887352@qq.com',
      long_description=readme_file(), url='https://XXX.com')
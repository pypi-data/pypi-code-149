from setuptools import setup

version = '0.0.1'

long_description = '''
GPT-Tools is a Python module that provides a comprehensive suite of tools for working with OpenAI's GPT-3 language model. 
The module includes functions for natural language processing, text generation, and conversation simulations. 
With GPT-Tools, you can easily integrate GPT-3 into your applications and projects, streamlining the process of developing language-based applications. 
The module is designed to be easy to use, with intuitive APIs that make working with GPT-3 a breeze. 
Whether you're a seasoned developer or just getting started, GPT-Tools is the perfect choice for anyone looking to leverage the power of OpenAI's GPT-3 in their work.
'''

setup(
    name='gpttools',

    version=version,

    packages=['gptools', 'gptools.modules'],
    install_requires=['openai'],

    url='https://github.com/meyiapir/gpt_tools',

    license='Apache License, Version 2.0, see LICENSE file',

    author='meyap',

    author_email='mmeyiapir@gmail.com',

    description='GPT-Tools - Easy-to-use Python module with tools for OpenAI GPT-3. Natural language processing, text generation, and conversation simulations included.',

    description_content_type='text/markdown',

    long_description=long_description,
    long_description_content_type='text/markdown',
)

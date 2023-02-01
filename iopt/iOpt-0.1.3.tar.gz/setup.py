from setuptools import setup, find_packages

with open("README.md") as file:
    read_me_description = file.read()

setup(
   name='iOpt',
   version='0.1.3',
   description='фреймворк для автоматического выбора значений параметров для математических моделей, ИИ и МО.',
   author='UNN Team',
   author_email='',
   long_description=read_me_description,
   long_description_content_type="text/markdown",
   url="https://github.com/UNN-ITMM-Software/iOpt",
   python_requires='>=3.7',
   packages=find_packages(),
   install_requires=['numpy>=1.19',
                     'depq',
                     'cycler',
                     'kiwisolver',
                     'matplotlib>=3.3.2',
                     'scikit-learn',
                     'sphinx_rtd_theme',
                     'readthedocs-sphinx-search',
                     'sphinxcontrib-details-directive',
                     'autodocsumm'],
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)

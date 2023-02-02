from setuptools import setup, find_packages


with open('README.md','r') as f:
  long_desc = f.read() 

setup(
    name='tfIdfInheritVectorizer',
    version='0.1',
    license='MIT',
    author="Berke Dilekoglu",
    long_description= long_desc,
    long_description_content_type='text/markdown',    
    packages=find_packages(),
    keywords='machine-learning tf-idf',
    test_suite="tests", 
    install_requires=[
        'numpy',
        'scikit-learn',
      ],

)
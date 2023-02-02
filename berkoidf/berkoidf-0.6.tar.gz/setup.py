from setuptools import setup, find_packages


with open('README.md','r') as f:
  long_desc = f.read() 

setup(
    name='berkoidf',
    version='0.6',
    license='MIT',
    author="Berke Dilekoglu",
    long_description= long_desc,
    long_description_content_type='text/markdown',
    url = 'https://github.com/berkedilekoglu/tfidfvectorizerinheritencecase',   
    download_url = 'https://github.com/berkedilekoglu/tfidfvectorizerinheritencecase/archive/refs/tags/vectorizer.tar.gz',    
    
    packages=find_packages(),
    keywords='machine-learning tf-idf',
    test_suite="tests", 
    install_requires=[
        'numpy',
        'scikit-learn',
      ],

)
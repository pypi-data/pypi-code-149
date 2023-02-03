from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='turtlepolish',
  version='1.0.0',
  description='This is turtle graphic library in Polish commands.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='DaytimeSpore380',
  author_email='michal.jakubiuk11@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='turtle polish',
  packages=find_packages(),
  install_requires=['PythonTurtle']
)
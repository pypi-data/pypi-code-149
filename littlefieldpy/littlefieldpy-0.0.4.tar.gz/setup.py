from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Education',
  'Topic :: Education',
  'Operating System :: Microsoft :: Windows',
  'Operating System :: MacOS',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(name='littlefieldpy',
      version='0.0.4',
      description='API for the Littlefield simulation',
      long_description=open('README.md').read() + '\n\n',
      url='http://github.com/AndrewKahr/littlefieldpy',
      keywords='littlefield',
      classifiers=classifiers,
      author='Andrew Kahr',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],
      zip_safe=False)

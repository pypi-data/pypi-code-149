from setuptools import setup, find_packages


setup(
    name='singlesignondemotest',
    version='0.4',
    author="lehonghieu1412159",
    author_email='lehonghieu1412159@gmail.com',
    packages=find_packages('.'),
    package_dir={'': '.'},
    url='https://github.com/lehonghieu1512/single-sign-on-demo',
    keywords='demo project',
    install_requires=[
          'django',
          'oauthlib',
          'pyOpenSSL',
          'requests'
      ],

)
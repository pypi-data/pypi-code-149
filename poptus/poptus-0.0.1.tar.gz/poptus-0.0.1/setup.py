from setuptools import setup

setup(
    name='poptus',
    version='0.0.1',    
    description='Practical Optimization Using Structure',
    url='https://github.com/poptus/',
    author='Jeffrey Larson and Stefan Wild',
    author_email='jmlarson@anl.gov',
    license='MIT',
    packages=['poptus'],
    package_dir={'poptus': 'pounders'},
    install_requires=['numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)

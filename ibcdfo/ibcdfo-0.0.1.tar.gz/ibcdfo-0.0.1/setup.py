from setuptools import setup

setup(
    name='ibcdfo',
    version='0.0.1',    
    description='Interpolation-Based Composite Derivative-Free Optimization',
    url='https://github.com/poptus/ibcdfo',
    author='Jeffrey Larson and Stefan Wild',
    author_email='jmlarson@anl.gov',
    license='MIT',
    packages=['ibcdfo'],
    package_dir={'ibcdfo': 'pounders'},
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

def configuration(parent_package='',top_path=None):

    from numpy.distutils.misc_util import Configuration
    config = Configuration('packageapple',parent_package,top_path)
    config.add_subpackage('math')
    return config



from setuptools import setup, find_packages

setup(
    name='packageapple',
    packages=find_packages(),
    version = 0.7,
    package = ['math']
)
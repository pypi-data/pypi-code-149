from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-dev',
    version='6.1.1',
    description='The core Reahl development tools.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-dev is the component containing general Reahl development tools. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.dev', 'reahl.dev_dev'],
    py_modules=[],
    include_package_data=False,
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=6.1,<6.2', 'reahl-tofu>=6.1,<6.2', 'reahl-stubble>=6.1,<6.2', 'reahl-sqlalchemysupport>=6.1,<6.2', 'Babel>=2.1,<2.11.999', 'Pygments>=2.1.0,<2.13.999', 'twine>=1.15.0,<4.0.9999', 'wheel>=0.34.0', 'tzlocal>=2.0.0,<4.2.9999', 'setuptools>=51.0.0', 'pip>=21.1', 'toml'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)

from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'graphviz', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-sqlalchemysupport', 'reahl-sqlitesupport', 'reahl-mysqlsupport'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-component',
    version='6.1.1',
    description='The component framework of Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThe reahl-component framework extends setuptools distribution packages to package and distribute more than just code. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.component', 'reahl.component_dev', 'reahl.messages'],
    py_modules=[],
    include_package_data=False,
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['Babel>=2.1,<2.11.999', 'python-dateutil>=2.8,<2.8.999', 'wrapt>=1.11.0,<1.14.999', 'setuptools>=51.0.0', 'pip>=21.1', 'cached-property>=1.5,<1.5.999;python_version<"3.8"', 'toml'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'graphviz', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-sqlalchemysupport', 'reahl-sqlitesupport', 'reahl-mysqlsupport'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)

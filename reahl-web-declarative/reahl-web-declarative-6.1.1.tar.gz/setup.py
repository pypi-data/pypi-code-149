from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'WebOb>=1.8,<1.8.999', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-webdev', 'reahl-browsertools', 'reahl-postgresqlsupport', 'reahl-domain'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-web-declarative',
    version='6.1.1',
    description='An implementation of Reahl persisted classes using SqlAlchemy.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nSome core elements of Reahl can be implemented for use with different persistence technologies. This is such an implementation based on SqlAlchemy. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.webdeclarative', 'reahl.webdeclarative_dev'],
    py_modules=[],
    include_package_data=True,
    namespace_packages=['reahl'],
    install_requires=['reahl-sqlalchemysupport>=6.1,<6.2', 'reahl-web>=6.1,<6.2', 'reahl-component>=6.1,<6.2'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'WebOb>=1.8,<1.8.999', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-webdev', 'reahl-browsertools', 'reahl-postgresqlsupport', 'reahl-domain'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)

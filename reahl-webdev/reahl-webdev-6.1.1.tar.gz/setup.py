from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-doc', 'reahl-postgresqlsupport'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-webdev',
    version='6.1.1',
    description='Web-specific development tools for Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl development tools for testing and working with web based programs. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.webdev', 'reahl.webdev_dev'],
    py_modules=[],
    include_package_data=True,
    namespace_packages=['reahl'],
    install_requires=['reahl-web>=6.1,<6.2', 'reahl-dev>=6.1,<6.2', 'reahl-component>=6.1,<6.2', 'reahl-tofu>=6.1,<6.2', 'selenium>=2.42,<4.7.9999', 'watchdog>=0.8.3,<2.2.999', 'WebOb>=1.8,<1.8.999', 'setuptools>=51.0.0', 'prompt_toolkit>=2.0.10,<3.0.999', 'cached-property>=1.5,<1.5.999;python_version<"3.8"'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-doc', 'reahl-postgresqlsupport'],
    extras_require={'pillow': ['Pillow>=2.5,<9.3.999']},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)

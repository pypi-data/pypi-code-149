from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'plotly>=5.1.0,<5.11.99999', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-webdev', 'reahl-browsertools', 'reahl-postgresqlsupport', 'reahl-sqlalchemysupport', 'reahl-web-declarative', 'reahl-domain'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-web',
    version='6.1.1',
    description='The core Reahl web framework',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis package contains the core of the Reahl framework.\n\nSee http://www.reahl.org/docs/current/tutorial/gettingstarted-install.d.html for installation instructions. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.messages', 'reahl.web', 'reahl.web.bootstrap', 'reahl.web.holder', 'reahl.web.static', 'reahl.web.static.jquery', 'reahl.web_dev', 'reahl.web_dev.advanced', 'reahl.web_dev.advanced.subresources', 'reahl.web_dev.appstructure', 'reahl.web_dev.bootstrap', 'reahl.web_dev.inputandvalidation', 'reahl.web_dev.widgets'],
    py_modules=[],
    include_package_data=True,
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['reahl-component>=6.1,<6.2', 'reahl-mailutil>=6.1,<6.2', 'ply>=3.8,<3.11.999', 'rjsmin>=1.2.0,<1.2.999', 'rcssmin>=1.1.0,<1.1.999', 'beautifulsoup4>=4.6,<4.11.999', 'WebOb>=1.8,<1.8.999', 'Babel>=2.1,<2.11.999', 'setuptools>=51.0.0', 'lxml>=4.2,<4.9.999', 'cached-property>=1.5,<1.5.999;python_version<"3.8"'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'plotly>=5.1.0,<5.11.99999', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-webdev', 'reahl-browsertools', 'reahl-postgresqlsupport', 'reahl-sqlalchemysupport', 'reahl-web-declarative', 'reahl-domain'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)

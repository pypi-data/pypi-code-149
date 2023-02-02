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
    name='reahl',
    version='6.1.1',
    description='The Reahl web framework.',
    long_description='Reahl is a web application framework for Python programmers.\n\nWith Reahl, programming is done purely in Python, using concepts familiar from GUI programming---like reusable Widgets and Events. There\'s no need for a programmer to know several different languages (HTML, JavaScript, template languages, etc) or to keep up with the tricks of these trades. The abstractions presented by Reahl relieve the programmer from the burden of dealing with the annoying problems of the web: security, accessibility, progressive enhancement (or graceful degradation) and browser quirks.\n\nReahl consists of many different eggs that are not all needed all of the time. This package does not contain much itself, but is an entry point for installing a set of Reahl eggs:\n\nInstall Reahl by installing with extras, eg: pip install "reahl[declarative,sqlite,dev,doc]" to install everything needed to run Reahl on sqlite, the dev tools and documentation.\n\nSee http://www.reahl.org/docs/current/tutorial/gettingstarted-install.d.html for installation instructions. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=[],
    py_modules=[],
    include_package_data=False,
    namespace_packages=[],
    install_requires=[],
    setup_requires=['pytest-runner', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'wheel'],
    tests_require=['pytest>=3.0'],
    extras_require={'all': ['reahl-component>=6.1,<6.2', 'reahl-web>=6.1,<6.2', 'reahl-mailutil>=6.1,<6.2', 'reahl-sqlalchemysupport>=6.1,<6.2', 'reahl-web-declarative>=6.1,<6.2', 'reahl-domain>=6.1,<6.2', 'reahl-domainui>=6.1,<6.2', 'reahl-postgresqlsupport>=6.1,<6.2', 'reahl-sqlitesupport>=6.1,<6.2', 'reahl-mysqlsupport>=6.1,<6.2', 'reahl-dev>=6.1,<6.2', 'reahl-webdev>=6.1,<6.2', 'reahl-browsertools>=6.1,<6.2', 'reahl-stubble>=6.1,<6.2', 'reahl-tofu>=6.1,<6.2', 'reahl-doc>=6.1,<6.2'], 'web': ['reahl-component>=6.1,<6.2', 'reahl-web>=6.1,<6.2', 'reahl-mailutil>=6.1,<6.2'], 'sqlite': ['reahl-sqlitesupport>=6.1,<6.2'], 'postgresql': ['reahl-postgresqlsupport>=6.1,<6.2'], 'mysql': ['reahl-mysqlsupport>=6.1,<6.2'], 'declarative': ['reahl-sqlalchemysupport>=6.1,<6.2', 'reahl-web-declarative>=6.1,<6.2', 'reahl-domain>=6.1,<6.2', 'reahl-domainui>=6.1,<6.2'], 'dev': ['reahl-dev>=6.1,<6.2', 'reahl-webdev>=6.1,<6.2', 'reahl-stubble>=6.1,<6.2', 'reahl-tofu>=6.1,<6.2'], 'doc': ['reahl-doc>=6.1,<6.2']},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)

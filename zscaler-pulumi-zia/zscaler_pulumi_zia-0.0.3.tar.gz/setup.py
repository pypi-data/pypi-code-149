# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.0.3"
PLUGIN_VERSION = "0.0.3"

class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'zia', PLUGIN_VERSION, '--server', 'github://api.github.com/zscaler'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print(f"""
                There was an error installing the zia resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource zia {PLUGIN_VERSION}`
                """)
            else:
                raise


def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "zia Pulumi Package - Development Version"


setup(name='zscaler_pulumi_zia',
      version=VERSION,
      description="A Pulumi package for creating and managing zia cloud resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      keywords='pulumi zia zscaler category/cloud',
      url='https://www.zscaler.com',
      project_urls={
          'Repository': 'https://github.com/zscaler/pulumi-zia'
      },
      license='MIT',
      packages=find_packages(),
      package_data={
          'zscaler_pulumi_zia': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)

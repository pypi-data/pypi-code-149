# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jetty_scorecard', 'jetty_scorecard.checks', 'jetty_scorecard.templates']

package_data = \
{'': ['*'], 'jetty_scorecard.checks': ['templates/*']}

install_requires = \
['inquirerpy>=0.3.4,<0.4.0',
 'jinja2>=3.1.2,<4.0.0',
 'networkx>=3.0,<4.0',
 'pandas>=1.5.3,<2.0.0',
 'snowflake-connector-python>=2.9.0,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['jetty_scorecard = jetty_scorecard:run']}

setup_kwargs = {
    'name': 'jetty-scorecard',
    'version': '0.1.4',
    'description': '',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/jettylabs/jetty_scorecard/main/etc/scorecard_logo.svg" alt="jetty scorecard logo" width="700" >\n</p>\n<br><br>\n\n# About Jetty Scorecard\n\n<p align="center">\n  <img src="https://raw.githubusercontent.com/jettylabs/jetty_scorecard/main/etc/scorecard_screenshot.png" alt="jetty scorecard screenshot" width="830" >\n</p>\n<br><br>\n\nIt can be hard to keep track of, not to mention follow, data infrastructure best practices - we want to change that!\n\nJetty Scorecard is living documentation of Snowflake best practices - it outlines recommendations with links to relevant documentation, and does so in the context of your existing environment. This makes it easy to know what you can do right now to improve your security and maintainability.\n\n# Getting Started\n\n### Installation\n\nInstall Jetty Scorecard with\n\n```bash\npip install jetty-scorecard\n```\n\n### Running Jetty Scorecard\n\nOnce installed, you can launch it by simply running\n\n```bash\njetty_scorecard\n```\n\nThis will take you through an interactive connection setup to connect to your Snowflake instance. You can authenticate using browser-based SSO, a password, or a private key.\n\n> **_NOTE:_** If you don\'t want to connect to Snowflake, you can still see the the best practices Scorecard looks for. Just run `jetty_scorecard -d` to generate a dummy scorecard to show an example scorecard (without any actual scores).\n\nOnce you\'ve authenticated with Snowflake, Scorecard will run for a few moments and then open up a browser with your results!\n\n### Interpreting your results\n\nEach result includes:\n\n-   A description of what is being checked\n-   Links to relevant documentation\n-   The queries used to run the check\n-   Specific insights into your roles, users, polices, and permissions to help you improve your configuration\n\n### Getting for updated results\n\nAfter making changes to your Snowflake environment, you can run Scorecard again. You can choose to go through the wizard again, or, if you\'d rather, you can include all of the relevant information on the command line (you can even do this the first time around!).\n\nAfter you run Scorecard the first time, it will print to your console a command that you can use to generate the scorecard again using the same configuration. You can also just read the CLI documentation by running\n\n```bash\njetty_scorecard --help\n```\n\n> If you think this is neat, give it a star, and share it with someone you know!\n\n# Contributing\n\nThis is just a first draft of Scorecard - there\'s so much more that can be done!\n\nDo you have ideas for additional best practices that should be included? Would you like to modify some that already exist? Do you have suggestions for the UI or UX?\n\nIf you have suggestions or comments, feel free to create an issue, open a pull request, or reach out in another way!\n\n# Security considerations\n\nUnless run in dummy mode (`jetty_scorecard -d`) Jetty Scorecard pulls metadata from your database, and so requires a database connection. To get holistic account-level data, it should be run with an administrator role, such as SECURITYADMIN or ACCOUNTADMIN (or another role with similar, though perhaps read-only privileges).\n\nTo provide peace of mind, it is worth noting that the Jetty Scorecard application:\n\n-   Does not capture and/or share usage analytics of any sort\n-   Does not write any credentials to disk\n-   Runs exclusively read-only queries\n\n# About Jetty Labs\n\nJetty Labs is reinventing access control for the data teams.\n\nOur principal offering, Jetty Core, integrates with tools from across the data stack and centralizes access control into a single, version-controlled interface. Jetty Core lets users configure access policies in code using the tools today\'s data owners know and love, and then deploy those configurations in seconds.\n\nTry it out today with `pip install jetty-core`\n\n### Learn more\n\n-   [Jetty Documentation](https://docs.get-jetty.com?utm_source=scorecard&utm_medium=python&utm_campaign=scorecard")\n-   [Jetty Demo Video (YouTube)](https://bit.ly/jetty-demo)\n-   [Jetty Homepage](https://www.get-jetty.com?utm_source=scorecard&utm_medium=python&utm_campaign=scorecard)\n\n### Get in touch\n\nIf any of this looks interesting, we\'d love to hear your feedback!! If you\'d be willing to chat, shoot us an email at [product@get-jetty.com](mailto:product@get-jetty.com) - if we end up having a conversation, we\'d love to send you a gift card to show our appreciation for your time.\n\n# Disclaimer\n\nJetty Scorecard is designed to be an informative tool to help users understand some of the best practices related to Snowflake account management. It is NOT designed to find every possible vulnerability and misconfiguration. Any configuration decisions, suggested by Jetty Scorecard or not, are ultimately up to each account\'s database administrators.\n\n#\n\n<p align="center">\n<img src="https://raw.githubusercontent.com/jettylabs/jetty_scorecard/main/etc/logo.svg" alt="jetty logo" width="50" >\n</p>\n',
    'author': 'Isaac Hales',
    'author_email': 'isaac.hales@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

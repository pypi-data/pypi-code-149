# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['killtimer']

package_data = \
{'': ['*']}

install_requires = \
['PyAudio>=0.2.13,<0.3.0',
 'desktop-notifier>=3.4.0,<4.0.0',
 'humanfriendly>=10.0,<11.0',
 'pytimeparse>=1.1.8,<2.0.0',
 'rich>=12.4.3,<13.0.0']

entry_points = \
{'console_scripts': ['killtimer = killtimer.main:main',
                     'killtimer-stats = killtimer.stats:main']}

setup_kwargs = {
    'name': 'killtimer',
    'version': '0.3.1',
    'description': 'Closes application after specified work interval',
    'long_description': '# Killtimer - do more working less!\nThis utility helps limit the amount of time devoted to work by keeping track of clearly defined work periods.\nIt\'s like a timer which cannot be stopped but will kill the passed command forcing the user to finish the job.\n\nThis may sound counterintuitive, but a lot of studies show that limiting time for a task forces the person to use the time more effectively.\n\n## Features\n- CLI interface\n- Three configurable effort levels:\n  - Minimal\n  - Work\n  - Overtime\n- Keep track of user-provided command and kill it if it has been running too long (after overtime)\n- Utilizes desktop notifications to inform users about the finished period\n- Optionally can play a sound when minimal effort/work period is done\n- Allow storing amount of work done as CSV file for further analysis \n\n## Install\n```console\n$ pip install [--user] killtimer\n```\n\n## Usage\n\n![Screencast](screencast.gif)\n\n```usage\nusage: killtimer [-h] [-m duration] [-w duration] [-o duration] [-l log_file] [-t title] [-s sound_file] [command [command ...]]\n\nClose application when time runs out\n\npositional arguments:\n  command               Executable (with arguments) to run (default: None)\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -m duration, --minimal-effort duration\n                        Minimal work duration (default: 0:10:00)\n  -w duration, --work duration\n                        Proper work duration (default: 1:00:00)\n  -o duration, --overtime duration\n                        Overtime duration (default: 0:15:00)\n  -l log_file, --log log_file\n                        Log file where to store amount of work done (default: None)\n  -t title, --title title\n                        Title to display above progress bars and configuration (default: None)\n  -s sound_file, --sound sound_file\n                        Sound file to play when minimal effort or work period is reached (default: None)\n```\n\nUsually you would want to create alias in your `*rc` file like:\n```shell\nalias blender-work="killtimer -m 10m -w 1h -o 10m -t \'Creative work\' -l /path/to/worklog.csv blender"\n```',
    'author': 'Paweł Żukowski',
    'author_email': 'p.z.idlecode@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/idle-code/killtimer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

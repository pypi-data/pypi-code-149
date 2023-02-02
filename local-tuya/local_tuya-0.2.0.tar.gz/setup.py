# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['local_tuya',
 'local_tuya.device',
 'local_tuya.domoticz',
 'local_tuya.domoticz.plugin',
 'local_tuya.domoticz.units',
 'local_tuya.protocol',
 'local_tuya.protocol.message',
 'local_tuya.protocol.message.handlers']

package_data = \
{'': ['*']}

install_requires = \
['concurrent-tasks>=1,<2', 'pycryptodomex>=3,<4', 'xmltodict>=0.13,<0.14']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4,<5']}

setup_kwargs = {
    'name': 'local-tuya',
    'version': '0.2.0',
    'description': 'Interface to Tuya devices over LAN.',
    'long_description': '# local-tuya\nInterface to Tuya devices over LAN.\n\nFeatures:\n- asynchronous methods and transport\n- persistent communication to the device\n- automatic remote device state updates (remotes can still be used)\n- configuratble of buffering for subsequent updates\n- constraints between device commands\n- Domoticz plugin using a dedicated thread\n\n> 💡 For now, only v3.3 is supported as I only own devices using this version.\n\n> ⚠️ This library does not provide support for getting the local key of the device.\n> See how to do that using any of those projects:\n> - [tuyapi](https://github.com/codetheweb/tuyapi)\n> - [tinytuya](https://github.com/jasonacox/tinytuya)\n> \n> Generous thanks to the maintainers of those tools for details on interfacing with Tuya devices.\n\n\n## Architecture\nThis library is composed of two main components:\n- the Tuya protocol\n- the device\n\n### Protocol\nThe protocol is responsible of handling communication details with the Tuya device.\nIts interface consists of an asynchronous method to update the device and accepts a callback to subscribe to state changes.\n\nSee [protocol module](./local_tuya/protocol).\n\n### Device\nThe device handles higher level functional logic such as buffering, constraints and specific device commands.\n\nSee [device module](./local_tuya/device).\n\n## Domoticz plugin tools\nSee [Domoticz module](./local_tuya/domoticz).\n',
    'author': 'Gabriel Pajot',
    'author_email': 'gab@les-cactus.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gpajot/local-tuya',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webhooks_bridge']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'aiofiles>=22.1.0,<23.0.0',
 'fastapi>=0.89.1,<0.90.0',
 'httpx>=0.23.3,<0.24.0',
 'uvicorn>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'webhooks-bridge',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Webhooks Bridge\nA simple webhook receiver that filters, transforms and forwards webhooks.\n\n## Install\n### pip\n```shell\npip install webhooks-bridge\nWEBHOOKS_BRIDGE_CONFIG_PATH=$PWD uvicorn webhooks_bridge.main:app --port 8080\n```\n### Docker\n```shell\nexport DATA_DIR=<YOUR_CONFIG_DIR>\ndocker run -p 8888:80 \\\n  --name webhooks-bridge \\\n  -e WEBHOOKS_BRIDGE_LOG_LEVEL=DEBUG \\\n  --mount type=bind,source=$DATA_DIR,target=/config \\\n  sebastiannoelluebke/webhooks-bridge:latest\n```\n## Usage\n\n### Forward\nBy default the webhooks get forwarded with the original body and the same Content-Type.\n```yaml\n# webhooks.yml\nmy-cool-webhook: # POST http://localhost:8000/my-cool-webhook\n  - url: "https://webhook-receiver-1/" \n  - url: "https://webhook-receiver-2/" # Forward to multiple receivers\n```\n### Filter\nUse jinja2 templates to filter the incoming webhooks. If any of the conditions fails the webhook will not be forwarded. You can access the following data from the incoming request: ```json, headers, form, content(body), query```.\n```yaml\n# webhooks.yml\nmy-cool-webhook: # POST http://localhost:8000/my-cool-webhook\n  - url: "https://webhook-receiver-3/api/webhook/SAHASDLITZENLXLHS"\n    conditions:\n      - "{% if json.NotificationUrl.object.Payment.alias.iban == \'DE123123123123213\' %}True{% else %}False{% endif %}"\n      - "{% if json.NotificationUrl.object.Payment.amount.value|float > 0 %}True{% else %}False{% endif %}"\n```\n### Transform\n```yaml\n# webhooks.yml\nmy-cool-webhook: # POST http://localhost:8000/my-cool-webhook\n  - url: "https://webhook-receiver-1/"\n    json:\n      amount: "{{ json.NotificationUrl.object.Payment.amount.value }}"\n      receiver: "{{ json.NotificationUrl.object.Payment.alias.iban }}"\n      sender: "{{ json.NotificationUrl.object.Payment.counterparty_alias.iban }}"\n      description: "{{ json.NotificationUrl.object.Payment.description }}"\n\n```\n### Custom headers\n```yaml\n# webhooks.yml\nmy-cool-webhook: # POST http://localhost:8000/my-cool-webhook\n  - url: "https://webhook-receiver-1/"\n    headers:\n      x-customer-header: "my-header-value"\n```\n### All in one\n```yaml\n# webhooks.yml\nmy-cool-webhook: # POST http://localhost:8000/my-cool-webhook\n  - url: "https://webhook-receiver-1/"\n    headers:\n      x-customer-header: "my-header-value"\n    json:\n      amount: "{{ json.NotificationUrl.object.Payment.amount.value }}"\n      receiver: "{{ json.NotificationUrl.object.Payment.alias.iban }}"\n      sender: "{{ json.NotificationUrl.object.Payment.counterparty_alias.iban }}"\n      description: "{{ json.NotificationUrl.object.Payment.description }}"\n      original_header: "{{ headers.x_my_header }}"\n      query_param_1: "{{ query.param1 }}"\n```\n### Forward files\nCurrently it is not possible to forward webhooks with attached files\n',
    'author': 'Sebastian Lübke',
    'author_email': 'github@luebke.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SebastianLuebke/webhooks-bridge',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)

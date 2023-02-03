# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mdspec']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mdspec',
    'version': '0.0.1',
    'description': 'Declarative plain-text specifications for objects',
    'long_description': '# mdspec\n"Declarative Model Specifications, from markdown-ish plain text files"\n\nLooking at defining models / object specification in "plain text"\nfor working w/ designers &amp; clients. \n\nThis is very much a hacky work-in-progress, / working out loud playground at the moment. \n\n# The big idea:\n\nGerkin is alright for describing functional requirements - but the whole\nidea of "given/when/then" is very process oriented - whereas on \nDjango / Wagtail / CMS based sites often have many objects defined\nwhich automatically implement a tonne of features. (ie, A Page model\nwith a few fields).\n\nThey\'re implemented declaratively, not functionally.\n\nCould we have something similar to gerkin for models / blocks that are declarative\nnot functional?\n\nAnd could we use a declarative style of specification, but in a plain-english type\nof format to facilitate that in a way that\'s easy to understand & share betweeen\ntechies & non-techies?\n\n## Example:\n(syntax subject to change)\n\n```markdown\n# HomePage\nHomePage is a Page Type.\nIt has these fields:\n - title : required, text, maximum 100 characters\n - banner image : optional\n - banner text : optional\n - contents (the main contents of the page...)\n\nThe contents fields is a StreamField.\nIt has these blocks:\n - richtext\n - image\n - raw-html\n - contact-form\n\n## Block definitions...\n\nrichtext is a Wagtail Block.\nIt has these fields:\n - contents\n - style\n\nimage is a Wagtail Block.\nIt has these fields:\n - image (the link to the image itself...)\n - caption\n - link\n\n...\n```\n\nWhich, in theory, is relatively easy to understand for non-techies,\nand renders nicely as markdown.  It can be rendered out, signed off,\netc.\n\nIt\'s structured though, so it can be parsed (by this project) into\nsomething we can then travese / execute as part of CI / tests.\n\nSo for instance, we can find each defined page type, check that it\nhas all required fields.\n\nWe could also have tests that check that the admin page for each page\ntype actually has all of those fields as form fields in the admin.\n\nOnce you get to anywhere where logic is involved (eg, templates, output)\nthen switching to gerken based cases makes a lot more sense, this\nspec type would just be for things which are structurely "defined" rather\nthan functionally implemented... (if that makes sense?)\n\n## Thoughts:\n\n- anything in brakets (like this) is considered a comment, and ignored?\n- markdown titles are ignored too.\n- how can we have nice sections for random implementaion notes?\n  maybe use markdown quotation `> text` blocks?  Should those be\n  stored to use as docstrings in generation? or better not?\n\n# to play:\n\n\n```sh\npython3 mdspec/parser.py examples/pages.md\n```\nand it should output a structured version of the contents.\n(There will be tests run with `make test` too - WIP...)\n\n# What could we do with this?\n\n- Use it just as a structured way to define models / pages / etc.\n- Get sign off from different teams (BE / FE / Design / client...)\n- Run acceptance tests automatically off the structured data.\n- Generate initial model python code / tests / templates / etc?\n',
    'author': 'Daniel Fairhead',
    'author_email': 'danthedeckie@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

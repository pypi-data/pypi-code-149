# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cai2']

package_data = \
{'': ['*']}

install_requires = \
['biopython>=1.80', 'click>=8.1.3', 'scipy>=1.10.0']

setup_kwargs = {
    'name': 'cai2',
    'version': '1.0.4',
    'description': 'Python implementation of codon adaptation index',
    'long_description': '### cai2 - Codon Adaptation Index\n\n[![DOI](https://joss.theoj.org/papers/10.21105/joss.00905/status.svg)](https://doi.org/10.21105/joss.00905) [![docs](https://readthedocs.org/projects/cai/badge/?version=latest)](https://cai.readthedocs.io/en/latest/) [![PyPI version](https://badge.fury.io/py/cai2.svg)](https://badge.fury.io/py/cai2)\n\nAn implementation of [Sharp and Li\'s 1987 formulation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC340524/pdf/nar00247-0410.pdf)\n\nof the [codon adaption index](https://en.wikipedia.org/wiki/Codon_Adaptation_Index).\n\nThis is an update of [cai](https://pypi.org/project/CAI) providing the same functionality, but now works with all python 3 versions. This version also has more tests, some derived from the Sharp and Li 1987 paper above.  \n\nThis module can be installed with the following command:\n\n\t\n\t$ pip install cai2\n\nUse:\n\nFinding the CAI of a sequence is easy:\n\n    from cai2 import CAI\n    CAI("ATG...", reference=["ATGTTT...", "ATGCGC...",...])\n    0.24948128951724224\n\nDetermining which sequences to use as the reference set is left to the user, though the [HEG-DB](http://genomes.urv.cat/HEG-DB/) is a great resource of highly expressed genes.\n\nCitation\n\n---\n\n  \n\nLee, B. D. (2018). Python Implementation of Codon Adaptation Index.\n\n*Journal of Open Source Software, 3* (30), 905.\n\n[<https://doi.org/10.21105/joss.00905>](https://doi.org/10.21105/joss.00905)\n\n:\n\n  \n\n@article{Lee2018,\n\ndoi = {10.21105/joss.00905},\n\nurl = {https://doi.org/10.21105/joss.00905},\n\nyear = {2018},\n\nmonth = {oct},\n\npublisher = {The Open Journal},\n\nvolume = {3},\n\nnumber = {30},\n\npages = {905},\n\nauthor = {Benjamin D. Lee},\n\ntitle = {Python Implementation of Codon Adaptation Index},\n\njournal = {Journal of Open Source Software}\n\n---\nThe original creator was [<benjamin_lee@college.harvard.edu>](mailto:benjamin_lee@college.harvard.edu).  This version was created by Björn Johansson as it is needed for optional functionality for [pydna](https://pypi.org/project/pydna).  \n\nReference\n\n---------\n\n Sharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure\nof directional synonymous codon usage bias, and its potential\napplications. *Nucleic Acids Research*, 15(3), 1281–1295.',
    'author': 'Benjamin Lee',
    'author_email': 'benjamin_lee@college.harvard.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)

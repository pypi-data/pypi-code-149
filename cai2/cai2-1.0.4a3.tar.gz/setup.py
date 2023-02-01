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
    'version': '1.0.4a3',
    'description': 'Python implementation of codon adaptation index',
    'long_description': 'Python Codon Adaptation Index\n=============================\n\n![DOI](http://joss.theoj.org/papers/8adf6bd9fd6391d5343d15ea0b6b6525/status.svg%0A%20:target:%20http://joss.theoj.org/papers/8adf6bd9fd6391d5343d15ea0b6b6525)\n![Docs](https://readthedocs.org/projects/cai/badge/?version=latest%0A%20:target:%20https://cai.readthedocs.io/en/latest/?badge=latest%0A%20:alt:%20Documentation%20Status)\n![Travis](https://travis-ci.org/Benjamin-Lee/CodonAdaptationIndex.svg?branch=master%0A%20:target:%20https://travis-ci.org/Benjamin-Lee/CodonAdaptationIndex)\n![CodeFactor](https://www.codefactor.io/repository/github/benjamin-lee/codonadaptationindex/badge/master%0A%20:target:%20https://www.codefactor.io/repository/github/benjamin-lee/codonadaptationindex/overview/master)\n![PyPI](https://img.shields.io/pypi/v/CAI.svg%0A%20:target:%20https://pypi.org/project/CAI/)\n\nAn implementation of [Sharp and Li\'s 1987\nformulation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC340524/pdf/nar00247-0410.pdf)\nof the [codon adaption\nindex](https://en.wikipedia.org/wiki/Codon_Adaptation_Index).\n\nInstallation\n------------\n\nThis module is available from PyPI and can be downloaded with the\nfollowing command:\n\n    $ pip install CAI\n\nTo install the latest development version:\n\n    $ pip install git+https://github.com/Benjamin-Lee/CodonAdaptationIndex.git\n\nQuickstart\n----------\n\nFinding the CAI of a sequence is easy:\n\n    >>> from CAI import CAI\n    >>> CAI("ATG...", reference=["ATGTTT...", "ATGCGC...",...])\n    0.24948128951724224\n\nSimilarly, from the command line:\n\n    $ CAI -s sequence.fasta -r reference_sequences.fasta\n    0.24948128951724224\n\nDetermining which sequences to use as the reference set is left to the\nuser, though the [HEG-DB](http://genomes.urv.cat/HEG-DB/) is a great\nresource of highly expressed genes.\n\nContributing and Getting Support\n--------------------------------\n\nIf you encounter any issues using CAI, feel free to [create an\nissue](https://github.com/Benjamin-Lee/CodonAdaptationIndex/issues).\n\nTo contribute to the project, please [create a pull\nrequest](https://github.com/Benjamin-Lee/CodonAdaptationIndex/pulls).\nFor more information on how to do so, please look at GitHub\'s\n[documentation on pull\nrequests](https://help.github.com/articles/about-pull-requests).\n\nCitation\n--------\n\nLee, B. D. (2018). Python Implementation of Codon Adaptation Index.\n*Journal of Open Source Software, 3* (30), 905.\n[<https://doi.org/10.21105/joss.00905>](https://doi.org/10.21105/joss.00905)\n:\n\n    @article{Lee2018,\n      doi = {10.21105/joss.00905},\n      url = {https://doi.org/10.21105/joss.00905},\n      year  = {2018},\n      month = {oct},\n      publisher = {The Open Journal},\n      volume = {3},\n      number = {30},\n      pages = {905},\n      author = {Benjamin D. Lee},\n      title = {Python Implementation of Codon Adaptation Index},\n      journal = {Journal of Open Source Software}\n\nContact\n-------\n\nI\'m available for contact at\n[<benjamin_lee@college.harvard.edu>](mailto:benjamin_lee@college.harvard.edu).\n\nReference\n---------\n\nSharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure\nof directional synonymous codon usage bias, and its potential\napplications. *Nucleic Acids Research*, 15(3), 1281–1295.\n',
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

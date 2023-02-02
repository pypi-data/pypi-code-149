# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastami']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1', 'scikit-learn>=1.2.0', 'scipy>=1.10.0']

setup_kwargs = {
    'name': 'fastami',
    'version': '0.2.0',
    'description': 'A Monte Carlo approximation to the adjusted and standardized mutual information for faster clustering comparisons',
    'long_description': '[![codecov](https://codecov.io/gh/mad-lab-fau/fastami/branch/main/graph/badge.svg?token=U379I88TBU)](https://codecov.io/gh/mad-lab-fau/fastami)\n# FastAMI\n\nA Monte Carlo approximation to the adjusted and standardized mutual information for faster clustering comparisons. You can use this package as a drop-in replacement for ``skleran.metrics.adjusted_mutual_info_score``, when the exact calculation is too slow, i.e. because of large datasets and large numbers of clusters.\n\n## Installation\n\n``fastami`` requires Python >=3.8. You can install ``fastami`` via pip from PyPI:\n\n```bash\npip install fastami\n```\n\n## Usage Examples\n\n### FastAMI\n\nYou can use FastAMI as you would use ``adjusted_mutual_info_score`` from ``scikit-learn``:\n\n```python\nfrom fastami import adjusted_mutual_info_mc\n\nlabels_true = [0, 0, 1, 1, 2]\nlabels_pred = [0, 1, 1, 2, 2]\n\nami, ami_error = adjusted_mutual_info_mc(labels_true, labels_pred)\n\n# Output: AMI = -0.255 +- 0.008\nprint(f"AMI = {ami:.3f} +- {ami_error:.3f}")\n```\n\nNote that the output may vary a little bit, due to the nature of the Monte Carlo approach. If you would like to ensure reproducible results, use the ``seed`` argument. By default, the algorithm terminates when it reaches an accuracy of ``0.01``. You can adjust this behavior using the ``accuracy_goal`` argument.\n\n### FastSMI\n\nFastSMI works similarly:\n\n```python\nfrom fastami import standardized_mutual_info_mc\n\nlabels_true = [0, 0, 1, 1, 2]\nlabels_pred = [0, 1, 1, 2, 2]\n\nsmi, smi_error = standardized_mutual_info_mc(labels_true, labels_pred)\n\n# Output: SMI = -0.673 +- 0.035\nprint(f"SMI = {smi:.3f} +- {smi_error:.3f}")\n```\n\nWhile FastSMI is usually faster than an exact calculation of the SMI, it is still orders of magnitude slower than FastAMI. Since the SMI is not confined to the interval ``[-1,1]`` like the AMI, the SMI by default terminates at a given absolute or relative error of at least ``0.1``, whichever is reached first. You can adjust this behavior using the ``precision_goal`` argument.\n\n## Citing FastAMI\n\nIf you use `fastami` in your research work, please cite the corresponding paper (will probably be published by March 2023):\n\n```\nKlede et al., (2023). FastAMI - A Monte Carlo Approach to the Adjustment for Chance in Clustering Comparison Metrics. Proceedings of the AAAI Conference on Artificial Intelligence.\n```\n',
    'author': 'FastAMI',
    'author_email': 'kai.klede@fau.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)

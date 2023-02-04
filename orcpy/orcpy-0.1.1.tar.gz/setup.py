# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orcpy', 'orcpy.design']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'orcpy',
    'version': '0.1.1',
    'description': 'A python package for designing organic Rankine cycles',
    'long_description': '<div align="center"> <img src="https://raw.githubusercontent.com/mehran-hmdpr/orcpy/main/orcpy.png" width="350" height="300" >\n\n<div align="left">\n\n# orcpy\n**orcpy**: A lightweight Python module that applies thermodynamic principles, analysing a given set of heat source and heat sink data to find the optimum design parameters of an organic Rankine cycle for waste heat recovery projects.\n\n\n\n## Table of contents\n* [Description](#description)\n     * [Problem definition](#problem-definition)\n     * [Problem solution](#problem-solution)\n\n* [Dependencies and installation](#dependencies-and-installation)\n\n* [Examples and Tutorials](#examples-and-tutorials)\n\n* [Authors and contributors](#authors-and-contributors)\n\n* [License](#license)\n\n## Description\n**orcpy** is a Python package which can come to your aid to deal with *Waste heat recovery* (WHR) projects. This package can give you the optimum pressure level, working fluid and mass flow rate to obtain maximum power generation and heat recovery, considering the constraints of your project such as the minimum allowable temperature of the waste heat stream and condenser.\n\n#### Problem definition\nFirst step is formalization of the problem in the **orcpy** framework. The optimization problem which orcpy is desigend to solve is shown below:\n\n\n*Maximization*   *f<sub>work<sub>* *(pressure level)*\n\n   *sub. to:*\n  \n\n  \n  *waste heat temperature > T<sub>dew<sub>*\n  \n  *temperature difference in heat exchangers* > $\\Delta$*T<sub>min<sub>*\n  \n  *evaporator pressure* < *0.85 P<sub>critical<sub>* \n  \n  *condenser temperature* > *T<sub>allowable<sub>*\n  \n  *condenser pressure* > *1 bar*\n          \n#### Problem solution\n  \nAfter defining it, we want of course to solve such a problem. To this aim, the orcpy package uses a golden section search approach to find the optimum pressure level between the upper (*0.85 P<sub>critical<sub>*) and the lower (*P<sub>condenser<sub>*) boundaries. The input variables that should be given to the orcpy are as follow:\n  \n- The inlet temperature for the waste stream (ºC)\n- The outlet temperature for the waste stream (ºC)\n- The power of the waste stream (kW)\n- The heat capacity of the waste stream (kW / ºC)\n- The minimum temperature of the condenser (ºC)\n- The minimum temperature difference (ºC)\n- Isentropic efficiencies of turbine and pump (%)\n\n  knowing these parameter, orcpy will give you optimum design parameters of the ORC system.\n  \n## Dependencies and installation\n**orcpy** requires `numpy`, `pandas`, `CoolProp`, `pina`, `plotly`. The code is tested for Python 3, while compatibility of Python 2 is not guaranteed anymore. It can be installed using `pip` or directly from the source code.\n\n### Installing via PIP\nTo install the package just type:\n```bash\n> pip install orcpy\n```\nTo uninstall the package:\n```bash\n> pip uninstall orcpy\n```\n## Examples and Tutorials\nTo use orcpy after installation of requierd packages just type:\n  ```bash\n> from orcpy import design\n  Results, figure = design.ORC.cycle("all")\n```\nNext, the orcpy will ask you input variables. instead of `"all"` you can also input a list of working fluids you want to analyze.  \n  \n## Authors and contributors\n**orcpy** is developed and mantained by\n* [Mehran Ahmadpour](mailto:mehran.hmdpr@gmail.com)\n\nunder the supervision of Prof. Ramin Roshandel and Prof. Mohammad B. Shafii\n\nContact us by email for further information or questions about **orcpy**, or suggest pull requests. Contributions improving either the code or the documentation are welcome!\n\n## License\n\nSee the [LICENSE](https://github.com/mehran-hmdpr/orcpy/blob/main/LICENSE) file for license rights and limitations (MIT).\n\n   \n',
    'author': 'Mehran Ahmadpour',
    'author_email': 'mehran.hmdpr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

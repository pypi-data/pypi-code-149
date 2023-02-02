# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snake_opencv',
 'snake_opencv.core',
 'snake_opencv.dnn',
 'snake_opencv.highgui',
 'snake_opencv.imgcodecs',
 'snake_opencv.imgproc',
 'snake_opencv.photo',
 'snake_opencv.videoio']

package_data = \
{'': ['*']}

install_requires = \
['opencv-python>=4.0,<5.0']

setup_kwargs = {
    'name': 'snake-opencv',
    'version': '0.1.0',
    'description': 'Snake case opencv with type annotations',
    'long_description': '# Snake-OpenCV\nSnake case OpenCV with type annotations for Python.\n\nNote: Still in early development\n\n## Install\n\n```sh\ngit clone https://github.com/cospectrum/snake-opencv.git\ncd snake-opencv && pip install .\n```\n\n## Usage\n```py\nimport snake_opencv as cv\n\nimage = cv.imread(path)\nimage = cv.cvt_color(image, cv.COLOR_BGR2RGB)\n\ncv.imshow(window_name, image) \n```\n',
    'author': 'cospectrum',
    'author_email': 'severinalexeyv@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)

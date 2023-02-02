from setuptools import setup, find_packages
VERSION = '0.0.1'
DESCRIPTION = 'An educational physics simulator'

# Setting up
setup(
    name="educational_physics_simulator",
    version=VERSION,
    author="Edward Hardy",
    author_email="<hardyedward18@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pygame', 'pymunk', 'pillow'],
    keywords=['python', 'physics', 'educational', 'pygame', 'tkinter', 'pymunk'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
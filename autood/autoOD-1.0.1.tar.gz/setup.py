from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='autoOD',
    version="1.0.1",
    description="Module to automate object detection process.",
    long_description_content_type="text/markdown",
    long_description=README,
    py_modules=['auto_od'],
    author='Elina Chertova',
    author_email='elas.2015@mail.ru',
    packages=find_packages(),
    keywords=['ObjectDetection', 'autoML'],
    include_package_data=True,
    # package_dir={'': 'auto_od'},
    package_data={'auto_od': ['core/zoo_models.csv']},
    # packages=find_packages('auto_od', include=[
    #         'core*', 'data_processing*', 'training*'
    #     ])
)

install_requires = [
    'imageio==2.22.4',
    'IPython==8.6.0',
    'pandas==1.5.1',
    'scikit-image==0.19.3',
    'opencv-python==4.6.0.66'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)

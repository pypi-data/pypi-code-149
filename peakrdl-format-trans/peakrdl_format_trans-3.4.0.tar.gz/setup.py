import os
import setuptools

#from distutils.core import setup
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

with open(os.path.join("peakrdl_format_trans", "__about__.py"), encoding='utf-8') as f:
    v_dict = {}
    exec(f.read(), v_dict)
    version = v_dict['__version__']

setuptools.setup(
    name='peakrdl_format_trans',
    version=version,
    author='jiangqingliu',
    author_email='jiangqingliu822@gmail.com',
    url='https://github.com/jiangqingliu88/peakrdl_format_trans',
    description=long_description,
    license='LICENSE',
    packages=['peakrdl_format_trans'],
    package_dir={'': '.'},
    include_package_data=True,
    entry_points = {
        "peakrdl.exporters": [
            'formattrans = peakrdl_format_trans.__peakrdl__:MyExporterDescriptor'
        ],
        "peakrdl.importers": [
            'formattrans = peakrdl_format_trans.__peakrdl__:MyImporterDescriptor'
        ]
    },
    install_requires=[
        # 'python>=3.6.0',
        # 'pandas>=0.10.0'
    ],
)

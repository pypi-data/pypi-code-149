import re
from setuptools import setup, find_packages


def extract_version():
    return re.search(
        r'__version__ = "([\d.]+)"',
        open('src/lumo_core/__init__.py', 'r', encoding='utf-8').read()).group(1)


if __name__ == '__main__':
    setup(
        name='lumo_core',
        version=extract_version(),
        description='library to manage your pytorch experiments.',
        long_description_content_type='text/markdown',
        url='https://github.com/pytorch-lumo/lumo-core',
        author='sailist',
        author_email='sailist@outlook.com',
        license_files=('LICENSE',),
        include_package_data=True,
        classifiers=[
            'Programming Language :: Python :: 3.9',
        ],
        package_dir={"": "src"},
        keywords='lumo_core',
        packages=find_packages('src'),
        entry_points={
            'console_scripts': [
                'lumo_core = lumo_core.cli.cli:main'
            ]
        },
    )

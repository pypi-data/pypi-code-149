from distutils.core import setup

if __name__ == "__main__":
    setup(
        name='packageball',
        package_dir = {
            'mySubPackage1': 'mySubPackage1',
            'mySubPackage2': 'mySubPackage2'},
        packages=['mySubPackage1', 'mySubPackage2'],
    )





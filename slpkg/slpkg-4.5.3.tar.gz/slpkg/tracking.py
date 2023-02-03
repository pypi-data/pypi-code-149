#!/usr/bin/python3
# -*- coding: utf-8 -*-

from slpkg.configs import Configs
from slpkg.views.ascii import Ascii
from slpkg.queries import SBoQueries
from slpkg.utilities import Utilities
from slpkg.dependencies import Requires


class Tracking(Configs, Utilities):
    """ Tracking of the package dependencies. """

    def __init__(self, flags: list):
        super(Configs, self).__init__()
        super(Utilities, self).__init__()
        self.flags = flags
        self.flag_pkg_version = ['-pv', '--pkg-version']
        self.ascii = Ascii()
        self.llc = self.ascii.lower_left_corner
        self.hl = self.ascii.horizontal_line
        self.vl = self.ascii.vertical_line
        self.color = self.colour()
        self.cyan = self.color['cyan']
        self.grey = self.color['grey']
        self.yellow = self.color['yellow']
        self.endc = self.color['endc']

    def packages(self, packages: list):
        """ Prints the packages dependencies. """
        print(f"The list below shows the packages with dependencies:\n")

        char = f' {self.llc}{self.hl}'
        sp = ' ' * 4
        for package in packages:
            pkg = f'{self.yellow}{package}{self.endc}'

            if self.is_option(self.flag_pkg_version, self.flags):
                pkg = f'{self.yellow}{package}-{SBoQueries(package).version()}{self.endc}'

            requires = Requires(package).resolve()
            how_many = len(requires)

            if not requires:
                requires = ['No dependencies']

            print(pkg)
            print(char, end='')
            for i, req in enumerate(requires, start=1):
                require = f'{self.cyan}{req}{self.endc}'

                if self.is_option(self.flag_pkg_version, self.flags):
                    require = f'{self.cyan}{req}{self.endc}-{self.yellow}{SBoQueries(req).version()}{self.endc}'

                if i == 1:
                    print(f' {require}')
                else:
                    print(f'{sp}{require}')

            print(f'\n{self.grey}{how_many} dependencies for {package}{self.endc}\n')

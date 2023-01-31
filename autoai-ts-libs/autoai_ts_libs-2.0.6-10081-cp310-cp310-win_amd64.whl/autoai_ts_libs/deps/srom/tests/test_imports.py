# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Utility to import all packages under SROM dynamically.
This utility is created to check presence of any cyclic dependencies.
It also checks if any dependency is missing in order to avoid any failure during runtime.
"""
import pkgutil
import sys

PACKAGE_TO_SKIP = ["srom.tests", "srom.rearch", "srom.pipeline.distribution.celery"]


def import_modules_from_srom():
    """
    Import modules from autoai_ts_libs.deps.srom folder
    """
    return_code = 0
    for loader, module_name, _ in pkgutil.walk_packages(["../../srom"], prefix="srom."):
        conditions = [package not in module_name for package in PACKAGE_TO_SKIP]
        if all(conditions):
            try:
                loader.find_module(module_name).load_module(module_name)
            except ModuleNotFoundError as mnfe:
                print("{} failed with {}".format(module_name, mnfe.msg))
                return_code = 1
            except ImportError as ipe:
                print("{} failed with {}".format(module_name, ipe.msg))
                return_code = 1

    return return_code


if __name__ == "__main__":
    sys.exit(import_modules_from_srom())
    import_modules_from_srom()

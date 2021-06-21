# -*- coding: utf-8 -*-
"""
    Setup file for pyforest.
    Use setup.cfg to configure your project.
"""
import sys

from pkg_resources import VersionConflict, require
from setuptools import setup
from src.pyforest.auto_import import setup as setup_auto_import

from src.pyforest.user_specific_imports import _load_user_specific_imports
#(globals_: dict, user_imports_path=USER_IMPORTS_PATH)

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup()
    setup_auto_import()
    # extensions cannot be installed because pyforest is only available after the installation
    _load_user_specific_imports(globes(), "my common use import.txt")

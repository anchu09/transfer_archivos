# -*- coding: utf-8 -*-
"""Top level package for {{cookiecutter.project_name}}."""
import os
from importlib import metadata
from pathlib import Path

__version__ = metadata.version("{{cookiecutter.package_name}}")

WORKDIR = Path(os.getenv("WORKDIR", Path.cwd()))
BASEPATH = Path(__file__).parent

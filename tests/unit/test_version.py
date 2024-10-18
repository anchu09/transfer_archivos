# -*- coding: utf-8 -*-
"""Test for version."""
from {{cookiecutter.package_name}} import __version__


def test_version() -> None:
    """Test version."""
    assert __version__ == "{{cookiecutter.version}}", "Version is not the expected one."

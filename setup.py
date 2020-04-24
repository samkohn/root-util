"""setup.py file for root_util."""

from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "VERSION")) as f_version:
    version = f_version.read()


setup(
    name="root-util",
    version=version,
    description="ROOT utilities for Python",
    author="Sam Kohn",
    author_email="skohn@lbl.gov",
    py_modules=["root_util"],
    python_requires=">=3",
)

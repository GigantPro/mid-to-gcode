#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: GigantPro
:license: The GPLv3 License (GPLv3)
:copyright: (c) 2023 Xiver organization
"""

with open("pyproject.toml", encoding="utf-8") as file:
    VERSION = file.read().split("=")[2].split('"')[1]

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mid_to_gcode",
    version=VERSION,
    author="GigantPro",
    author_email="gigantpro2000@gmail.ru",
    description=("The project for translate .mid format to 3d printers gcode "),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GigantPro/mid_to_gcode",
    license="The GPLv3 License (GPLv3)",
    packages=["mid_to_gcode"],
    install_requires=[],
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
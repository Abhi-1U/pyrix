# -*- coding : UTF-8 -*-
from setuptools import setup, find_packages

NAME = "pyrix"
# *---------------------------------------------------------------------------*
# * Including ReadMe Markdown File in the setup
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
# *---------------------------------------------------------------------------*
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/Abhi-1U/pyrix/issues",
    "Documentation": "https://abhi-1u.github.io/pyrix-docs/",
    "Source Code": "https://github.com/Abhi-1U/pyrix",
}
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Operating System :: OS Independent",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Scientific/Engineering",
]
setup(
    name=NAME,
    license="MIT",
    version="0.7.19",
    author="Abhi-1U",
    author_email="PerricoQ@outlook.com",
    description="A matrix Library",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    project_urls=PROJECT_URLS,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    python_requires=">=3.0",
)

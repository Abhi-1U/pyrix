from setuptools import setup, find_packages

name = "pyrix"
# *---------------------------------------------------------------------------*
# * Including ReadMe Markdown File in the setup
with open("README.md", "r") as fh:
    long_description = fh.read()
# *---------------------------------------------------------------------------*
PROJECT_URLS = {
    "Documentation": "https://abhi-1u.github.io/gitlas/docs/",
    "Source Code": "https://github.com/Abhi-1U/gitlas",
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
    name=name,
    license="MIT",
    version="0.7.16rc0",
    author="Abhi-1U",
    author_email="PerricoQ@outlook.com",
    description="A matrix Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls=PROJECT_URLS,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    python_requires=">=3.0",
)

# DevOps Exercise

This is a skeleton repository for your exercise.
The goal of this exercise is to implement a Python package for sorting integer
lists using the DevOps software development approach.

> **Warning**: If working on windows, some directories and files in this archive
> will not be visible because they start with a '.'. In the file browser, change
> the View to display "Hidden items".

You will need to:

1. Add .pre-commit-config.yml which:
   1. Limits maximal file size.
   1. Runs the black and flake8 linters.
   1. Detect presence of aws credentials private keys.
1. Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory,
   code should be documented using standard Python practices (there are several [docstring
   styles](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
   select one and be consistent).
1. Implement testing using the [pytest](https://docs.pytest.org/en/6.2.x/) framework, see test directory.
1. Implement linting, style checking using both [flake8](https://flake8.pycqa.org/en/latest/) and
   [black](https://black.readthedocs.io/en/stable/).
1. Modify the GitHub actions workflow so that it tests and builds the package for all
   three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about [Distributing Python packages](https://docs.python.org/3/distributing/index.html).
1. Modify this file to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
1. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
   > **Warning**: Do not upload to the authoritative Python Package Index (PyPI).

Possible work division, three sub-teams:

1. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
1. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
1. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).

## Developer Installation

Clone the repository and change directory into it:

```bash
git clone https://github.com/MoodyMakai/CapstoneHW5.git
cd CapstoneHW5
```

It is reccomended to setup a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the developer requirements and pre-commit:
`make`

If you don't have make:

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
```
tests can be run with:
`pytest`

## Developer Usage and Guidelines

This repository is linted using black and flake8 formatters. It also has a max file size of 500kb.

To check if your code complies with standards, run: `pre-commit run --all-files`

pre-commit should also run automatically when commiting.


## Table of Testing Times 
_________________________________________________________________
|Operating System | Python Version  |  Test Time  |  Total Time |  
|_________________|_________________|_____________|_____________|
|  Mac            |  3.9            |  63.04s     |  116s       |
|_________________|_________________|_____________|_____________|
|  Mac            |  3.10           |  70.19s     |  116s       |
|_________________|_________________|_____________|_____________|
|  Windows        |  3.9            |  79.50s     |  133s       |
|_________________|_________________|_____________|_____________|
|  Windows        |  3.10           |  74.30s     |  120s       |
|_________________|_________________|_____________|_____________|
|  Ubuntu/Linux   |  3.9            |  75.38s     |  93s        |
|_________________|_________________|_____________|_____________|
|  Ubuntu/Linux   |  3.10           |  69.70s     |  88s        |
|_________________|_________________|_____________|_____________|
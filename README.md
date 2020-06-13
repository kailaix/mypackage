# MyPackage

A simple template for making Python packages with C/C++ extensions. 

## Overview

This is a simple example for making a Python package with C/C++ extensions. The package is made with

* **Building system**: the standard `setup.py` approach with specific instructions for compiling C/C++ source codes. 
* **Unit Test**: the standard `unittest` module. 
* **Documentation**: rendering Markdown documentation using [`mkdocs`](https://github.com/mkdocs/mkdocs)

## Workflow


The basic workflow is as follows:

* Install dependencies

```bash
pip install pytest
pip install mkdocs
```

* Implement codes (Python and C/C++) in `mypackage` directory. Look up the source codes for instructions. They are well documented. 

* Implement unit test in `test` directory. Basically you need to inherit from `unittest.TestCase` for new test cases.

* Add executable files to `bin` as you wish. After the user install the package, users will be able to use the executable files located in the `bin` directory. 

* Finally, implement `setup.py`. See the script for instructions. 


After you have done all the installation work, you can now install a development version using 

```bash 
pip install -e .
```

And then run the test

```bash
py.test
```

To make documents, run 


* Preview doc: `mkdocs serve`
* Build doc: `mkdocs build`



## Using `mypackage`


`mypackage` provides a binary executable `cr`, and you can execute this executable via 

```bash
cr
```

If you want to use `mypackage` in Python, you can import the package, e.g.,

```python
import mypackage
from mypackage import *
import mypackage.core as core 
```
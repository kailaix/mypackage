from setuptools import setup 
import subprocess
import os, sys, shutil 
from sys import platform
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

if  os.path.isdir(os.path.join("mypackage", "src", "build")):
    shutil.rmtree(os.path.join("mypackage", "src", "build"))
os.mkdir(os.path.join("mypackage", "src", "build"))

if platform.startswith('win32'):
    subprocess.Popen(
    """cmd /c cd mypackage\\src\\build &&\
    cmake -A x64 .. &&\
    cmake --build . --config Release""")
else:
    os.system(
        """cd mypackage/src/build &&\
        cmake .. &&\
        make -j
        """
    )


setup(
    name = "mypackage",
    version = "0.1.0",
    scripts = ['bin/cr', 'bin/cr.bat'], # the executables will be placed in the Python `bin` directory
    description = "An example pacakge.", 
    install_requires = ["numpy"],
    author = "Kailai Xu",
    author_email = "kailaix@hotmail.com"
)
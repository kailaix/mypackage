from ctypes import *
import os 
import numpy as np 
from sys import platform

dir_path = os.path.dirname(os.path.realpath(__file__))


# Load dynamic libraries
if platform.startswith("win"):
    libpath = os.path.join(dir_path, "src", "build", "sum")
else:
    libpath = os.path.join(dir_path, "src", "build", "libsum")
_lib = CDLL(libpath)

# We pass numpy arrays as pointers to C++
c_double_p = POINTER(c_double)


def mysum(a):
    # IMPORTANT: we need to set the input and output types of the C++ function 
    _lib.sum.argtypes  = [c_double_p, c_int]
    _lib.sum.restype = c_double 
    n = a.shape[0]
    # This is how to get the raw pointer of a numpy array
    a_ = a.ctypes.data_as(c_double_p)
    return _lib.sum(a_, n)

def inplace_accumulate(a):
    _lib.inplace_accumulate.argtypes = [c_double_p, c_int]
    _lib.inplace_accumulate.restype = c_double_p
    n = a.shape[0]
    a_ = a.ctypes.data_as(c_double_p)
    _lib.inplace_accumulate(a_, n)
    return a

from ctypes import *
import os 
import numpy as np 

dir_path = os.path.dirname(os.path.realpath(__file__))


libpath = os.path.join(dir_path, "src", "build", "sum.dll")
_lib = CDLL(libpath)

c_double_p = POINTER(c_double)


def mysum(a):
    _lib.sum.argtypes  = [c_double_p, c_int]
    _lib.sum.restype = c_double 
    n = a.shape[0]
    a_ = a.astype(np.float64).ctypes.data_as(c_double_p)
    return _lib.sum(a_, n)

def inplace_accumulate(a):
    _lib.inplace_accumulate.argtypes = [c_double_p, c_int]
    _lib.inplace_accumulate.restype = c_double_p
    n = a.shape[0]
    a_ = a.astype(np.float64).ctypes.data_as(c_double_p)
    _lib.inplace_accumulate(a_, n)
    return a

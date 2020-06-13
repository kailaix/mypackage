import unittest
import numpy as np 
from mypackage.core import mysum 
import mypackage.core as mc 


class TestMySum(unittest.TestCase):
    def test(self):
        a = np.random.rand(20)
        s = a.sum()
        self.assertLessEqual(abs(mysum(a)-s), 1e-8)


class TestAccSum(unittest.TestCase):
    def test(self):
        a = np.random.rand(20)
        s = a.cumsum()
        np.alltrue(mc.inplace_accumulate(a) == s)
import unittest
import numpy as np 
from mypackage.core import mysum 
import mypackage.core as mc 


class TestMySum(unittest.TestCase):
    def test(self):
        a = np.random.rand(20)
        s = a.sum()
        self.assertEqual(mysum(a), s)


class TestAccSum(unittest.TestCase):
    def test(self):
        a = np.random.rand(20)
        s = a.cumsum()
        np.alltrue(mc.inplace_accumulate(a) == s)
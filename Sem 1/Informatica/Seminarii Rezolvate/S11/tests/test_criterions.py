import unittest
from utils.criterions import *


class TestSearch(unittest.TestCase):
    def testIsEven(self):
        self.assertTrue(isEven(4))
        self.assertTrue(isEven(-8))
        self.assertFalse(isEven(1))
        self.assertFalse(isEven(-5))

    def testIsArmstrong(self):
        self.assertTrue(isArmstrong(0))
        self.assertTrue(isArmstrong(153))
        self.assertFalse(isArmstrong(12))
        self.assertFalse(isArmstrong(-50))

    def testIsPrime(self):
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(5))
        self.assertTrue(isPrime(13))
        self.assertFalse(isPrime(0))
        self.assertFalse(isPrime(1))
        self.assertFalse(isPrime(-9))

    def testIsPerfectSquare(self):
        self.assertTrue(isPerfectSquare(4))
        self.assertTrue(isPerfectSquare(1))
        self.assertTrue(isPerfectSquare(0))
        self.assertFalse(isPerfectSquare(3))
        self.assertFalse(isPerfectSquare(5))
        self.assertFalse(isPerfectSquare(-9))

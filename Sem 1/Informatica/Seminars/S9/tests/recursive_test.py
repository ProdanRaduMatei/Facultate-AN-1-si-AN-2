from unittest import TestCase
from logic.recursive import *


class RecursiveFunctionsTest(TestCase):
    def testFactorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertRaises(ValueError, factorial, 0)  # => factorial(0)

    def testFibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(6), 8)
        self.assertRaises(ValueError, fibonacci, -1)

    def testMultiplication(self):
        self.assertEqual(multiplication(0), 0)
        self.assertEqual(multiplication(1), 3)
        self.assertEqual(multiplication(3), 9)
        self.assertRaises(ValueError, multiplication, -1)

    def testSum(self):
        self.assertEqual(sum(0), 0)
        self.assertEqual(sum(1), 1)
        self.assertEqual(sum(4), 10)
        self.assertIsNone(sum(-1))

    def testPascal(self):
        self.assertEqual(pascal(1), [1])
        self.assertEqual(pascal(2), [1, 1])
        self.assertEqual(pascal(3), [1, 2, 1])
        self.assertIsNone(pascal(-1))

    def testMinimum(self):
        self.assertIsNone(minimum([]))
        self.assertEqual(minimum([1,5,3]), 1)
        self.assertEqual(minimum([1,-5,3]), -5)

    def testMaximum(self):
        self.assertIsNone(maximum([]))
        self.assertEqual(maximum([1,5,3]), 5)
        self.assertEqual(maximum([1,-5,3]), 3)

    def testRecursiveMin(self):
        self.assertIsNone(recursiveMin([[]]))
        self.assertEqual(recursiveMin([1, 2, 3, [-1, 5, [[-5]]]]), -5)
        self.assertEqual(recursiveMin([1, 2, 3, [-1]]), -1)
        self.assertEqual(recursiveMin([1, 2, 3, [-1], []]), -1)

    def testCount(self):
        self.assertEqual(count(2, []), 0)
        self.assertEqual(count(2, [1, 2, 3]), 1)
        self.assertEqual(count(2, [1, [2], 3, [[1, 2, 3]]]), 2)

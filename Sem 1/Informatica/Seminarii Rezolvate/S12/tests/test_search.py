import unittest
from utils.search import *
from utils import criterions


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.unordered = [1, 9, 5, 8, 4, 2, 3, 0, 15]
        self.ordered = sorted(self.unordered)

    def testSequentialSearchUnordered(self):
        self.assertEqual(sequentialSearchUnordered(self.unordered, 6), -1)
        self.assertEqual(sequentialSearchUnordered(self.unordered, 1), 0)
        self.assertEqual(sequentialSearchUnordered(self.unordered, 8), 3)

    def testSequentialSearchOrdered(self):
        self.assertEqual(sequentialSearchOrdered(self.ordered, 6), -1)
        self.assertEqual(sequentialSearchOrdered(self.ordered, 1), 1)
        self.assertEqual(sequentialSearchOrdered(self.ordered, 8), 6)

    def testBinarySearch(self):
        self.assertEqual(binarySearch(self.ordered, 6), -1)
        self.assertEqual(binarySearch(self.ordered, 1), 1)
        self.assertEqual(binarySearch(self.ordered, 8), 6)

    def testMyFilter(self):
        self.assertEqual(myFilter(self.unordered, criterions.isEven), [8, 4, 2, 0])
        self.assertEqual(myFilter(self.ordered, criterions.isEven), [0, 2, 4, 8])
        self.assertEqual(myFilter(self.unordered, criterions.isArmstrong), [1, 0])
        self.assertEqual(myFilter(self.ordered, criterions.isArmstrong), [0, 1])
        self.assertEqual(myFilter(self.unordered, criterions.criterion_i_2), [0])
        self.assertEqual(myFilter(self.ordered, criterions.criterion_i_2), [0])
        self.assertEqual(myFilter(self.unordered, criterions.criterion_i_3), [1, 9, 5, 8, 4, 2, 3, 0])
        self.assertEqual(myFilter(self.ordered, criterions.criterion_i_3), [0, 1, 2, 3, 4, 5, 8, 9])

    def testInBuiltFilter(self):
        self.assertEqual(inBuiltFilter(self.unordered, criterions.isEven), [8, 4, 2, 0])
        self.assertEqual(inBuiltFilter(self.ordered, criterions.isEven), [0, 2, 4, 8])
        self.assertEqual(inBuiltFilter(self.unordered, criterions.isArmstrong), [1, 0])
        self.assertEqual(inBuiltFilter(self.ordered, criterions.isArmstrong), [0, 1])
        self.assertEqual(inBuiltFilter(self.unordered, criterions.criterion_i_2), [0])
        self.assertEqual(inBuiltFilter(self.ordered, criterions.criterion_i_2), [0])
        self.assertEqual(inBuiltFilter(self.unordered, criterions.criterion_i_3), [1, 9, 5, 8, 4, 2, 3, 0])
        self.assertEqual(inBuiltFilter(self.ordered, criterions.criterion_i_3), [0, 1, 2, 3, 4, 5, 8, 9])

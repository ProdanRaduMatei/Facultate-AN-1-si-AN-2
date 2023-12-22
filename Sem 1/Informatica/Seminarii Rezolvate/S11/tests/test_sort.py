import unittest
from utils.sort import *


class TestSort(unittest.TestCase):
    def setUp(self):
        # containing input and output pairs
        self.lists = [
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([3, 2, 1], [1, 2, 3]),
            ([], []),
            ([6, 4, 7, 1, 3, 2, 5], [1, 2, 3, 4, 5, 6, 7])
        ]

    def testBubbleSort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubbleSort(input_list), output_list)

    def testMinimumSelectionSort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubbleSort(input_list), output_list)

    def testMaximumSelectionSort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubbleSort(input_list), output_list)

    def testInsertionSort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(bubbleSort(input_list), output_list)

    def testRecursiveQuickSort(self):
        for input_list, output_list in self.lists:
            self.assertEqual(recursiveQuickSort(input_list), output_list)

    # def testIterativeQuickSort(self):
    #     for input_list, output_list in self.lists:
    #         self.assertEqual(iterativeQuickSort(input_list), output_list)

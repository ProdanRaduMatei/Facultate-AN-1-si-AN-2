from unittest import TestCase
from domain import vectors as v
import numpy as np


class TestVector(TestCase):
    def setUp(self):
        self.vector = v.Vector('A', 'b', 1, [1, 2, 3, 4, 5])

    def testCreateVector(self):
        self.assertEqual(self.vector.name_id, 'A')
        self.assertEqual(self.vector.colour, 'b')
        self.assertEqual(self.vector.type, 1)

    def testSetName_ID(self):
        self.vector.name_id = 'A'
        self.assertEqual(self.vector.name_id, 'A')

    def testSetColour(self):
        self.vector.colour = 'b'
        self.assertEqual(self.vector.colour, 'b')

    def testSetType(self):
        self.vector.type = 1
        self.assertEqual(self.vector.type, 1)

    def testSetValues(self):
        self.vector.values = [2]
        self.assertEqual(self.vector.values, [2])

    def testStringRepresentation(self):
        self.assertEqual(str(self.vector), "Vector(A, b, 1, [1, 2, 3, 4, 5])")

    def testAddScalar(self):
        self.vector.values = [1, 3, 4]
        new_list = list(np.array(self.vector.values + 2))
        print(new_list)
        self.assertEqual(new_list, [3, 5, 6])

    def testAddTwoVectors(self):
        self.vector.values = [1, 2, 3]
        new_list = list(np.array(self.vector.values + [1, 2, 3]))
        print(new_list)
        self.assertEqual(new_list, [2, 4, 6])

    def testSubtractTwoVectors(self):
        self.vector.values = [2, 3, 4]
        new_list = list(np.array(self.vector.values - [1, 1, 1]))
        print(new_list)
        self.assertEqual(new_list, [1, 2, 3])

    def testMultiplyTwoVectors(self):
        self.vector.values = [1, 2, 3]
        value = float(np.sum(np.multiply(np.array(self.vector.values), [1, 2, 3])))
        print(value)
        self.assertEqual(value, 14)

    def testSumOfElements(self):
        self.vector.values = [1, 3, 4]
        sum_of_elements = float(np.sum(self.vector.values))
        print(sum_of_elements)
        self.assertEqual(sum_of_elements, 8)

    def testProdOfElements(self):
        self.vector.values = [1, 3, 4]
        prod_of_elements = float(np.product(self.vector.values))
        print(prod_of_elements)
        self.assertEqual(prod_of_elements, 12)

    def testAverageOfElements(self):
        self.vector.values = [1, 2, 3]
        avg = float(np.average(self.vector.values))
        print(avg)
        self.assertEqual(avg, 2)

    def testMinOfElements(self):
        self.vector.values = [1, 2, 3]
        minn = float(np.min(self.vector.values))
        print(minn)
        self.assertEqual(minn, 1)

    def testMaxOfElements(self):
        self.vector.values = [1, 3, 4]
        maxx = float(np.max(self.vector.values))
        print(maxx)
        self.assertEqual(maxx, 4)


class TestRepository(TestCase):
    def setUp(self):
        self.repo1 = v.VectorRepository([
            v.Vector('A', 'b', 1, [5, 9, 6]),
            v.Vector('B', 'r', 2, [8]),
            v.Vector('C', 'y', 3, [9, 7]),
            v.Vector('D', 'm', 4, []),
            v.Vector('E', 'g', 5, [4, 6]),
        ])
        self.repo2 = v.VectorRepository([
            v.Vector('F', "b", 1, []),
            v.Vector('G', "r", 2, [8]),
            v.Vector('H', "y", 3, [8, 6]),
            v.Vector('I', "m", 4, [5]),
            v.Vector('J', "g", 1, [4, 8]),
            v.Vector('K', "r", 2, [8, 7, 6]),
            v.Vector('L', "b", 3, [7]),
        ])

    def testCreateVectorRepository(self):
        self.assertEqual(v.VectorRepository.getVectors(self.repo1), 5)
        self.assertEqual(v.VectorRepository.getVectors(self.repo2), 7)

    def testAddVector(self):
        self.repo1.addVector('Z', 'b', 2, [2, 3, 4, 1])
        self.assertEqual(v.VectorRepository.getVectors(self.repo1), 6)

    def testUpdateVectorAtIndex(self):
        self.repo1.updateAtIndex(1, 'g', 2, [8,4,2,1])
        print("wgrighiorhgiowriogior")
        print(self.repo1.getAtIndex(1))
        self.assertEqual(str(self.repo1.getAtIndex(1)), "Vector(B, g, 2, [8, 4, 2, 1])")



    def testUpdateVectorByID(self):
        self.repo2.updateByID('H','g', 1, [7,6,4])
        print(self.repo2.getID('H'))
        self.assertEqual(str(self.repo2.getAtIndex(self.repo2.getID('H'))), "Vector(H, g, 1, [7, 6, 4])")

    def testDeleteAtIndex(self):
        self.repo1.deleteAtIndex(1)
        self.assertEqual(self.repo1.getVectors(), 4)

    def testDeleteByID(self):
        self.repo2.deleteByID('H')
        self.assertEqual(self.repo2.getVectors(), 6)



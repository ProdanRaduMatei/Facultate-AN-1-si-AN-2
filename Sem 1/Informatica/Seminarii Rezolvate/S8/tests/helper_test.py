from unittest import TestCase
from utils import helpers as h


class HelperTestClass(TestCase):
    def testCheckGrade(self):
        self.assertTrue(h.checkGrade(5))
        self.assertEqual(h.checkGrade(5), True)
        self.assertFalse(h.checkGrade(0))
        self.assertFalse(h.checkGrade(11))

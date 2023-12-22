'''
Created on Jan, 2023

@author: Mathew
'''
import unittest

from domain.patient import Patient
from domain.department import Department
from application.departmentValidator import DepartmentValidator
class DepartmentValidatorTest(unittest.TestCase):

    def testValidate(self):
        '''
        Checks the validator.
        '''
        p1 = Patient("Pop", "Andrei", "123456", "coughing")
        p2 = Patient("Pop", "Ioana", "293456", "fever")
        l = [p1, p2]
        d = Department(-2, "Simple diseases", 2, l)
        v = DepartmentValidator()
        try:
            v.validate(d)
            assert False
        except Exception:
            assert True

        d = Department(9, "Simple diseases", 2, l)
        try:
            v.validate(d)
            assert True
        except ValueError:
            assert False
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
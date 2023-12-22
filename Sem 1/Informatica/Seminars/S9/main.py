import unittest
from logic.data_examples import printAll

loader = unittest.TestLoader()
suite = loader.discover("./tests", pattern="*_test.py")
unittest.TextTestRunner(verbosity=2).run(suite)
input("Enter to see data examples.")
printAll()

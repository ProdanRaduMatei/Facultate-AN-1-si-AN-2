import unittest
if __name__ == "__main__":
    """
    This is how you can run all of you tests at once. You have to load them with a `TestLoader` (class in `unittest`). For the `discover` method you have to pass:
        - directory: where to look for the files containing the test classes (in my case `test` directory in the current - '.' - folder) 
        - pattern (optional argument): a pattern that matches the test files' name (in my case it has to start with 'tests_' and it has the finish with '.py')
    """
    loader = unittest.TestLoader()
    suite = loader.discover("./test", pattern="*_tests.py")
    unittest.TextTestRunner().run(suite)

    # or run in the console the following command
    # python -m unittest discover -s test -p 'tests_*.py'
    
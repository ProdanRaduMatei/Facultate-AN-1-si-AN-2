from test.tests import TestVector as runAllVectorTests
from test.tests import TestRepository as runAllRepositoryTests


def runAllTests():
    runAllVectorTests()
    runAllRepositoryTests()
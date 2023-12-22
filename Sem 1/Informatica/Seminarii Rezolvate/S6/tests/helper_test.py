from utils.helpers import *


def testCheckGrade():
    assert not checkGrade(0)
    assert not checkGrade(12)
    assert checkGrade(5)


def runAllTests():
    testCheckGrade()

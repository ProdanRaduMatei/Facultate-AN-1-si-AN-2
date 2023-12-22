from utils.helpers import *


def testMaximumGrade():
    assert maximumGrade([]) == 0
    assert maximumGrade([['a', 6], ['b', 6]]) == 6
    assert maximumGrade([['a', 6], ['b', 7]]) == 7


def testIsPalindrome():
    assert isPalindrome("")
    assert isPalindrome("a")
    assert isPalindrome("asddsa")
    assert isPalindrome("asdda") == False

def runAllTests():
    testMaximumGrade()
    testIsPalindrome()

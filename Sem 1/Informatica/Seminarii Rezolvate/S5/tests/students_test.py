# import domain.students
# domain.students.printStudents([])

# from domain import students
# students.printStudents([])

# from domain import students as ss
# ss.printStudents([])

from domain.students import *
# printStudents([])


def testAddStudents():
    students = []
    addStudent(students, ['asd', 5])
    assert students == [['asd', 5]]

    try:
        addStudent(students, ['asd', 1, 2])
        assert False
    except ValueError:
        assert True

    try:
        addStudent(students, ['asd'])
        assert False
    except ValueError:
        assert True

    try:
        addStudent(students, ['asd', 0])
        assert False
    except ValueError:
        assert True

    try:
        addStudent(students, ['asd', 11])
        assert False
    except ValueError:
        assert True


def testFindStudentByName():
    assert findStudentByName([], 'asd') == -1
    assert findStudentByName([['asd', 6]], 'asd') == 0
    assert findStudentByName([['def', 6], ['asd', 8], ['asd', 3]], 'asd') == 1


def testDeleteStudentByName():
    assert deleteStudentByName([], 'asd') == False
    assert deleteStudentByName([['asd', 6]], 'asd') == True
    assert deleteStudentByName([['def', 6], ['asd', 8], ['asd', 3]], 'asd') == True


def testFilterGradeHigher():
    for i in range(1, 11):
        assert filterGradeHigher([], i) == []

    assert filterGradeHigher([['a', 5], ['b', 6], ['c', 7]], 5) == [['b', 6], ['c', 7]]
    assert filterGradeHigher([['a', 5], ['b', 6], ['c', 7]], 8) == []


def testFilterStudentsMaxGrade():
    assert filterStudentsMaxGrade([]) == []
    assert filterStudentsMaxGrade([['a', 6]]) == [['a', 6]]
    assert filterStudentsMaxGrade([['a', 6], ['b', 8], ['c', 8]]) == [['b', 8], ['c', 8]]


def testGetStudentNamesStartWith():
    assert getStudentNamesStartWith([], "") == []
    assert getStudentNamesStartWith([], "a") == []
    assert getStudentNamesStartWith([["a", 7], ["b", 9]], "a") == [["a", 7]]
    assert getStudentNamesStartWith([["a", 7], ["b", 9]], "") == [["a", 7], ["b", 9]]


def testRemoveStudentsWithSmallerGrade():
    assert removeStudentsWithSmallerGrade([], 5) == []
    assert removeStudentsWithSmallerGrade([["a", 7], ["b", 9]], 5) == [["a", 7], ["b", 9]]
    assert removeStudentsWithSmallerGrade([["a", 7], ["b", 9]], 7) == [["a", 7], ["b", 9]]
    assert removeStudentsWithSmallerGrade([["a", 7], ["b", 9]], 8) == [["b", 9]]


def testRemoveStudentsWithPalindromeName():
    assert removeStudentsWithPalindromeName([]) == []
    assert removeStudentsWithPalindromeName([["a", 7]]) == []
    assert removeStudentsWithPalindromeName([["as", 7]]) == [["as", 7]]


def testNameFrequency():
    assert nameFrequency([], "a") == 0
    assert nameFrequency([["a", 7]], "a") == 1
    assert nameFrequency([["a", 7], ["b", 8], ["a", 9]], "a") == 2

def runAllTests():
    testAddStudents()
    testFindStudentByName()
    testDeleteStudentByName()
    testFilterGradeHigher()
    testFilterStudentsMaxGrade()
    testGetStudentNamesStartWith()
    testRemoveStudentsWithSmallerGrade()
    testRemoveStudentsWithPalindromeName()
    testNameFrequency()
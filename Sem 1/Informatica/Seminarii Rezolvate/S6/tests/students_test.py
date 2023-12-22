# import domain.students
# domain.students.printStudents([])

# from domain import students
# students.printStudents([])

# from domain import students as ss
# ss.printStudents([])

from domain.students import *
# printStudents([])


def testCreateStudent():
    try:
        Student(1, "A", 0)
        assert False
    except ValueError:
        assert True


def testGettersAndSetters():
    s = Student(1, "A", 5)
    assert s.getName() == "A"
    assert s.name == "A"
    assert s.getId() == 1
    assert s.id == 1
    assert s.getGrade() == 5
    assert s.grade == 5

    s.setId(2)
    assert s.getId() == 2
    assert s.id == 2
    s.setName("B")
    assert s.getName() == "B"
    assert s.name == "B"
    s.setGrade(10)
    assert s.getGrade() == 10
    assert s.grade == 10
    try:
        # testing if error is raised when grade is not correct
        s.setGrade(0)
        assert False
    except ValueError:
        assert True
    try:
        # testing if error is raised when grade is not correct
        s.setGrade(100)
        assert False
    except ValueError:
        assert True

    s.id = 3
    assert s.getId() == 3
    assert s.id == 3
    s.name = "C"
    assert s.getName() == "C"
    assert s.name == "C"
    s.grade = 8
    assert s.getGrade() == 8
    assert s.grade == 8
    try:
        # testing if error is raised when grade is not correct
        s.grade = 0
        assert False
    except ValueError:
        assert True
    try:
        # testing if error is raised when grade is not correct
        s.grade = 100
        assert False
    except ValueError:
        assert True


def testCreateStudentRepository():
    sr = StudentRepository()
    assert sr.getStudentCount() == 0
    sr = StudentRepository([Student(1, "A", 5)])
    print(sr)
    assert sr.getStudentCount() == 1


def testAddStudentToRepository():
    sr = StudentRepository()
    assert sr.getStudentCount() == 0
    sr.addStudent(1, "A", 5)
    assert sr.getStudentCount() == 1
    try:
        # testing if error is raised when inserting a duplicate id
        sr.addStudent(1, "B", 7)
        assert False
    except ValueError:
        assert True


def testInsertStudentToRepository():
    sr = StudentRepository()
    assert sr.getStudentCount() == 0
    sr.insertStudent(0, 1, "A", 5)
    assert sr.getStudentCount() == 1
    try:
        # testing if error is raised when index is not correct
        sr.insertStudent(-1, 2, "B", 7)
        assert False
    except IndexError:
        assert True
    try:
        # testing if error is raised when index is not correct
        sr.insertStudent(100, 3, "C", 4)
        assert False
    except IndexError:
        assert True
    try:
        # testing if error is raised when inserting a duplicate id
        sr.insertStudent(0, 1, "D", 9)
        assert False
    except ValueError:
        assert True


def testGetStudentIndexById():
    s1 = Student(1, "A", 5)
    s2 = Student(2, "B", 7)
    rs = StudentRepository([s1, s2])
    assert rs.getIndexOfStudent(1) == 0
    assert rs.getIndexOfStudent(2) == 1
    assert rs.getIndexOfStudent(3) == -1


def runAllTests():
    testCreateStudent()
    testGettersAndSetters()

    testCreateStudentRepository()
    testAddStudentToRepository()
    testInsertStudentToRepository()
    testGetStudentIndexById()

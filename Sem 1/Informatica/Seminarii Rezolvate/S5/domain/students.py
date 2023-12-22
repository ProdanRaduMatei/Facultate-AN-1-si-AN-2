import utils.helpers as help

def printStudents(students):
    """
    ex. 1.
    Print all student in the list.
    :param students: given list of students containing name s and grades
    :type students: list
    """
    if len(students) == 0:
        print("There are no students in the list!")
    for x in students:
        print("Name = ", x[0], "\tgrade = ", x[1])


def addStudent(students, newStudent):
    """
    ex. 2.
    Add a new student to the list
    :param students: list of students
    :type students: list
    :param newStudent: list representing the student
    :type newStudent: list
    :return:
    :rtype:
    """
    if len(newStudent) != 2:
        raise ValueError("the value is not valid")
    if not 1 <= newStudent[1] <= 10:
        raise ValueError("incorrect grade")
    students.append(newStudent)


def findStudentByName(students, name):
    """
    ex. 3.
    Find the index of a given student by name
    :param students: list of students
    :type students: list
    :param name: name of the searched student
    :type name: str
    :return: position of the student
    :rtype: int
    """
    for i,x in enumerate(students) :
        if x[0]==name:
            return i
    return -1


def deleteStudentByName(students, name):
    """
    ex. 4.
    Delete a student from the list with the given name
    :param students: given list of students
    :type students: list
    :param name: name of the student
    :type name: str
    :return:
    :rtype: bool
    """
    positionOfStudent = findStudentByName(students, name)
    if positionOfStudent==-1:
        return False
    students.pop(positionOfStudent)
    # del students[positionOfStudent]
    return True

def filterGradeHigher(students, minimumGrade):
    """
    Get students from the list with grade higher than the given value
    :param students: list of students
    :type students: list
    :param minimumGrade:
    :type minimumGrade: int
    :return: selected students
    :rtype: list
    """
    final=[]
    for i in students:
        if i[1]>minimumGrade:
            final.append(i)
    return final

def filterStudentsMaxGrade(students):
    """
    ex. 6.
    :param students: list od students
    :type students: list
    :return: students with maximum grade
    :rtype: list
    """
    x=help.maximumGrade(students)
    maxStudents=[]
    for i in students:
        if i[1]==x:
            maxStudents.append(i)
    return maxStudents


def getStudentNamesStartWith(students, substring):
    """
    ex. 8:
    Get all students with names starting with the given substring
    :param students: list of students
    :type students: list
    :param substring:
    :type substring: str
    :return: filtered list of students
    :rtype: list
    """
    std = []
    for i in students:
        if i[0][:len(substring)] == substring:
            std += [i]
        # if i[0].startswith(substring):
        #     std += [i]
    return std


def removeStudentsWithSmallerGrade(students, maxValue):
    """
    ex. 9.
    Remove students with grade smaller than a given value
    :param students: list of students
    :type students: list
    :param maxValue: max grade in the list
    :type maxValue: int
    :return: modified list of students
    :rtype: list
    """
    i=0
    while i < len(students):
        if students[i][1] < maxValue:
            students.pop(i)
        else:
            i += 1

    return students


def removeStudentsWithPalindromeName(students):
    """
    ex. 10.
    Delete students for which the name is a palindrome
    :param students: list of students
    :type students: list
    :return: modified list
    :rtype: list
    """
    i=0
    while i < len(students):
        if help.isPalindrome(students[i][0]):
            del students[i]
        else:
            i += 1

    return students


def nameFrequency(students, name):
    """
    ex. 1..
    Define the frequency of a given name in the list of students
    :param students: list of students
    :type students: list
    :param name: given name
    :type name: str
    :return: occurrence of the name among the students
    :rtype: int
    """
    i=0
    counter=0
    while i<len(students):
        if students[i][0]==name:
            counter+=1
        i += 1
    return counter


def writeIntoFile(students, filename):
    """
    Write the list of students into the specified file
    :param students: list of students
    :type students: list
    :param filename: name of the result file
    :type filename: str
    """
    f = open(filename, "w")
    for student in students:
        f.write(student[0] + " " + str(student[1]) + "\n")
    f.close()

def readFromFile(filename):
    """
    Read a list of students from the given file
    :param filename: name of the file
    :type filename: str
    :return: list of students
    :rtype: list
    """
    f = open(filename, "r")
    students = []
    for line in f:
        attr = line.split()
        if len(attr) != 2:
            # raise some error
            pass
        addStudent(students, [attr[0], int(attr[1])])
    f.close()
    return students
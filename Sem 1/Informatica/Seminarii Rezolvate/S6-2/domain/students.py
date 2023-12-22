import utils.helpers as h


class Student:
    def __init__(self, id_, name, grade):
        """
        Create a student object with id, name and grade
        :param id_:
        :type id_: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        """
        self.__id = id_
        self.__name = name
        if h.checkGrade(grade):
            self.__grade = grade
        else:
            raise ValueError("grade is not correct!")

    # getter functions for the properties
    def getName(self):
        """
        Get the name of the student
        :return:
        :rtype: str
        """
        return self.__name

    def getId(self):
        """
        Get the id of the student
        :return:
        :rtype: int
        """
        return self.__id

    def getGrade(self):
        """
        Get the grade of the student
        :return:
        :rtype: int
        """
        return self.__grade

    # the name of the function becomes the name of the property
    # refer as s.name
    @property
    def name(self):
        """
        Get the name of the student
        :return:
        :rtype: str
        """
        return self.__name

    @property
    def id(self):
        """
        Get the id of the student
        :return:
        :rtype: int
        """
        return self.__id

    @property
    def grade(self):
        """
        Get the grade of the student
        :return:
        :rtype: int
        """
        return self.__grade

    # setter function for the properties
    def setName(self, newName):
        """
        Set the name of the student
        :return:
        :rtype: str
        """
        self.__name = newName

    def setId(self, newId):
        """
        Set the id of the student
        :return:
        :rtype: int
        """
        self.__id = newId

    def setGrade(self, newGrade):
        """
        Set the grade of the student
        :return:
        :rtype: int
        """
        if h.checkGrade(newGrade):
            self.__grade = newGrade
        else:
            raise ValueError("grade is not correct")

    # the name of the function should be the same as the name of the property
    @name.setter
    def name(self, newName):
        """
        Set the name of the student
        :return:
        :rtype: str
        """
        self.__name = newName

    @id.setter
    def id(self, newId):
        """
        Set the id of the student
        :return:
        :rtype: int
        """
        self.__id = newId

    @grade.setter
    def grade(self, newGrade):
        """
        Set the grade of the student
        :return:
        :rtype: int
        """
        if h.checkGrade(newGrade):
            self.__grade = newGrade
        else:
            raise ValueError("grade is not correct")

    def __repr__(self):
        """
        Return the string representation of the student.
        :return:
        :rtype:
        """
        # return "Student(" + str(self.__id) + ", " + self.__name + ", " + str(self.__grade) + ")"
        return f"Student({self.__id}, {self.__name}, {self.__grade})"

    def __str__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Check if two student objects are equal by comparing the their properties
        :param other:
        :type other: Student
        :return:
        :rtype: bool
        """
        return self.__id == other.__id and self.__name == other.__name and self.__grade == other.__grade


class StudentRepository:
    def __init__(self, initialStudents=None):
        """
        Creating a repository containing students
        """
        self.__listOfStudents = []
        if initialStudents is not None:
            # check if the ids are unique
            for student in initialStudents:
                if isinstance(student, Student) and self.__isIdUnique(student.id):
                    self.__listOfStudents.append(student)

    def addStudent(self, id_, name, grade):
        """
        S6. ex. 1
        Add a new student to the repository
        :param id_:
        :type id_: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        :return:
        :rtype:
        """
        if not self.__isIdUnique(id_):
            raise ValueError("This id is already in the list!")
        else:
            self.__listOfStudents.append(Student(id_, name, grade))

    def insertStudent(self, index, id_, name, grade):
        """
        S6. ex. 2
        Insert a new student to the repository
        :param index:
        :type index: int
        :param id_:
        :type id_: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        :return:
        :rtype:
        """
        if not self.__isIdUnique(id_):
            raise ValueError("This id is already in the list!")
        elif not self.__isIndexCorrect(index):
            raise IndexError("The index is not correct")
        else:
            self.__listOfStudents.insert(index, Student(id_, name, grade))

    def getStudentCount(self):
        """
        S6. ex. 3
        Get the number of students in the repostiroy
        :return:
        :rtype: int
        """
        return len(self.__listOfStudents)

    def getIndexOfStudent(self, id_):
        """
        S6. ex. 4
        Get the index of a student identified by his/her id.
        :param id_:
        :type id_: int
        :return:
        :rtype: int
        """
        for index, student in enumerate(self.__listOfStudents):
            if student.getId() == id_:
                return index
        return -1

    def getStudents(self):
        """
        S6. ex. 5
        Get all students from the repository.
        Return a copy of the list! Otherwise, the user can change the content of the list.
        :return:
        :rtype: list
        """
        return self.__listOfStudents[:]

    def getAtIndex(self, index):
        """
        S6. ex. 6.
        Get student at a specified index.
        :param index:
        :type index: int
        :return:
        :rtype: Student
        """
        if self.__isIndexCorrect(index):
            return self.__listOfStudents[index]
        else:
            raise IndexError(f"Index is not correct!")

    def __getitem__(self, index):
        return self.getAtIndex(index)

    def getByID(self, id_):
        """
        S6. ex. 7.
        get student by id
        :param id_:
        :type id_: int
        :return:
        :rtype: Student
        """
        if self.__isIdUnique(id_):
            raise ValueError
        else:
            return self.getAtIndex(self.getIndexOfStudent(id_))

    def getStudentsGradeLess(self, maxGrade):
        """
        S6. ex. 8.
        Get all students with grade less than the given value
        :param maxGrade:
        :type maxGrade: int
        :return:
        :rtype: StudentRepository
        """
        selectedStudents = []
        for student in self.__listOfStudents:
            if student.grade < maxGrade:
                selectedStudents.append(student)
        return StudentRepository(selectedStudents)

    def updateAtIndex(self, index, name, grade):
        """
        S6. ex. 9.
        Update a student at a given index
        :param index:
        :type index: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        """
        if self.__isIndexCorrect(index):
            student = self.getAtIndex(index)
            # only if you have a setter defined with annotation
            # @name.setter
            # def name(self, name):
            #   ...
            student.name = name
            student.grade = grade
        else:
            raise IndexError("Index is not correct")

    def updateByID(self, id_, name, grade):
        """
        S6. ex. 10.
        Update a student at a given index
        :param id_:
        :type id_: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        """
        self.updateAtIndex(self.getIndexOfStudent(id_), name, grade)

    def deleteAtIndex(self, index):
        """
        S6. ex. 11.
        Update a student at a given index
        :param index:
        :type index: int
        """
        if self.__isIndexCorrect(index):
            del self.__listOfStudents[index]
        else:
            raise IndexError("Index is not correct")

    def deleteByID(self, id_):
        """
        S6. ex. 12.
        Update a student at a given index
        :param id_:
        :type id_: int
        """
        self.deleteAtIndex(self.getIndexOfStudent(id_))

    def __isIndexCorrect(self, index):
        """
        Check if the index is correct in the list of student
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__listOfStudents) or 0 == index == len(self.__listOfStudents)

    def __isIdUnique(self, id_):
        """
        Check if the given id is already in the list.
        :param id_:
        :type id_: int
        :return:
        :rtype: bool
        """
        for student in self.__listOfStudents:
            if student.getId() == id_:
                return False
        return True

    def __repr__(self):
        """
        Return the string representation of the class.
        :return:
        :rtype: str
        """
        if len(self.__listOfStudents) == 0:
            return "No students!"
        else:
            str_repr = ""
            for student in self.__listOfStudents:
                str_repr += str(student) + "\n"
            return str_repr


if __name__ == "__main__":
    s = Student(1, 'A', 6)
    print(s)

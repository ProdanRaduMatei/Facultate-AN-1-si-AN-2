from domain import students
from tests import runAllTests


def dataExamples():
    listOfStudents = [["Adel", 7], ["Maria", 10], ["Andrei", 9], ["Paul", 6], ["Cristi", 8]]
    print("ex.1.")
    students.printStudents(listOfStudents)

    print("ex.2.")
    students.addStudent(listOfStudents, ["Marian", 7])
    students.printStudents(listOfStudents)

    print("ex.3.")
    print(students.findStudentByName(listOfStudents, "Cristi"))

    print("ex.4.")
    print(students.deleteStudentByName(listOfStudents, "Adel"))
    students.printStudents(listOfStudents)

    print("ex.5.")
    students.printStudents(students.filterGradeHigher(listOfStudents, 5))
    print()
    students.printStudents(students.filterGradeHigher(listOfStudents, 8))

    print("ex.6.")
    students.printStudents(students.filterStudentsMaxGrade(listOfStudents))
    listOfStudents[0][1] = 9
    print()
    students.printStudents(students.filterStudentsMaxGrade(listOfStudents))


def printMenu():
    print("MENU:")
    print("-2 - print data examples")
    print("-1 - print menu")
    print(" 0 - exit program")
    print(" 1 - add a new student")
    print("...")
    print(" 8 - get students name starting with given prefix")
    print(" 9 - remove students with grade smaller than a given value")
    print("10 - remove students with palindrome name")
    print("...")



def start():
    runAllTests()
    print("All tests run successfully!")
    print()
    my_students = []
    printMenu()
    command = None
    while command != 0:  # while True
        try:
            command = int(input(">>> "))
            if command == -2:
                dataExamples()
            elif command == -1:
                printMenu()
            elif command == 0:
                print("program ended")
            elif command == 1:
                name = input("Name of the student: ")
                grade = input("Grade of the student: ")
                try:
                    grade = int(grade)
                    if 1 <= grade <= 10:
                        students.addStudent(my_students, [name, grade])
                        students.printStudents(my_students)
                    else:
                        print("grade should be between 1 and 10, but", grade), "given!"
                except ValueError:
                    print("The grade should be an integer!")
            elif command == 2:
                pass
            elif command == 8:
                substring = input("Prefix of the names: ")
                students.printStudents(students.getStudentNamesStartWith(my_students, substring))
            elif command == 9:
                maxValue = int(input("Maximum grade in the list: "))
                students.removeStudentsWithSmallerGrade(my_students, maxValue)
                students.printStudents(my_students)
            elif command == 10:
                students.printStudents(students.removeStudentsWithPalindromeName())
            elif command == 15:
                filename = input("Name of the file: ")
                students.writeIntoFile(my_students, filename)
            elif command == 16:
                filename = input("Name of the file: ")
                my_students = students.readFromFile(filename)
                students.printStudents(my_students)
            else:
                print("invalid command")
        except ValueError:
            print("invalid type entered!")


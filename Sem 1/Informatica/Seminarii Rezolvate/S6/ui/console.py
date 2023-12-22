from domain import students as s
from tests import runAllTests


def dataExamples():
    repo = s.StudentRepository([s.Student(1, "Andrei", 5), s.Student(2, "Maria", 7), s.Student(3, "Paul", 6),
                                s.Student(4, "Mihai", 8), s.Student(5, "Ana", 10), s.Student(6, "Catalin", 10),
                                s.Student(7, "Ioana", 4), s.Student(8, "Alexandru", 9), s.Student(9, "Madalina", 6),
                                s.Student(10, "Sonia", 3)])
    print(repo)

    print("ex.1.")
    print("add a new student: Student(11, 'Claudia', 7)")
    repo.addStudent(11, "Claudia", 7)
    print(repo)
    print("add a new student: Student(5, 'Mircea', 8)")
    try:
        repo.addStudent(5, 'Mircea', 8)
    except ValueError as ve:
        print(ve)
    print(repo)

    print("ex.2.")
    print("insert a new student: Student(12, 'Gabriela', 6) at index 3")
    repo.insertStudent(3, 12, 'Gabriela', 6)
    print(repo)
    print("insert a new student: Student(13, 'Stefan', 7) at index -1")
    repo.insertStudent(-1, 13, 'Stefan', 7)
    print(repo)

    print("ex.3.")
    print(f"index of student with id 5 is {repo.getIndexOfStudent(5)}")
    print(f"index of student with id 12 is {repo.getIndexOfStudent(12)}")
    print(f"index of student with id 20 is {repo.getIndexOfStudent(20)}")

    print("ex.4.")
    print(f"number of students in the list {repo.getStudentCount()}")


def printMenu():
    print("MENU:")
    print("-2 - print data examples")
    print("-1 - print menu")
    print(" 0 - exit program")
    print(" 1 - add a new student")
    print(" 2 - insert new student")
    print(" 3 - get student count")
    print(" 4 - get student index by id")
    print(" 5 - get students")


def start():
    runAllTests()
    print("All tests run successfully!")
    print()
    stud_repo = s.StudentRepository()
    printMenu()
    command = None
    while command != 0:  # while True
        try:    # catches all conversion errors
            command = int(input(">>> "))
            if command == -2:
                dataExamples()
            elif command == -1:
                printMenu()
            elif command == 0:
                print("program ended")
            elif command == 1:
                id_ = int(input("Id of the student: "))
                name = input("Name of the student: ")
                grade = int(input("Grade of the student: "))
                try:
                    stud_repo.addStudent(id_, name, grade)
                    print(stud_repo)
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                index = int(input("Index of the student: "))
                id_ = int(input("Id of the student: "))
                name = input("Name of the student: ")
                grade = int(input("Grade of the student: "))
                try:
                    stud_repo.insertStudent(index, id_, name, grade)
                    print(stud_repo)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
            elif command == 3:
                print(f"Number of students in the list: {stud_repo.getStudentCount()}")
            elif command == 4:
                id_ = int(input("Id of the student: "))
                print(f"Index of the student by the specific id {id_}: {stud_repo.getIndexOfStudent(id_)}")
            elif command == 5:
                print(stud_repo.getStudents())
            else:
                print("invalid command")
        except ValueError:
            print("invalid type entered!")


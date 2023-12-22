from domain import students as s


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
    try:
        repo.insertStudent(-1, 13, 'Stefan', 7)
    except IndexError:
        print("Index -1 is not correct! Student is not added")
    print(repo)

    print("ex.3.")
    print(f"index of student with id 5 is {repo.getIndexOfStudent(5)}")
    print(f"index of student with id 12 is {repo.getIndexOfStudent(12)}")
    print(f"index of student with id 20 is {repo.getIndexOfStudent(20)}")

    print("ex.4.")
    print(f"number of students in the list {repo.getStudentCount()}")

    print("ex.5.")
    print("Students in the repo as list:", repo.getStudents())

    print("ex.6.")
    print(repo)
    print(f"student at index 4 is {repo[4]}")
    try:
        print("student at index 15 is", end=" ")
        repo.getAtIndex(15)
    except IndexError:
        print("not defined in the repository!")

    print("ex.7.")
    print(f"student with ID 6 is {repo.getByID(6)}")
    try:
        print("student with ID 15 is", end=" ")
        repo.getAtIndex(15)
    except IndexError:
        print("not defined in the repository!")

    print("ex.8.")
    print(f"students with grade less than 5 are\n{repo.getStudentsGradeLess(5)}")
    print(f"students with grade less than 5 are\n{repo.getStudentsGradeLess(1)}")
    print(f"students with grade less than 5 are\n{repo.getStudentsGradeLess(8)}")

    print("ex.9.")
    print(repo)
    print(f"update student at index 4 with name Test1 and grade 4")
    repo.updateAtIndex(4, "Test1", 4)
    print(f"now the student at index 4 is {repo[4]}")
    try:
        print(f"update student at index 50 with name Test2 and grade 6")
        repo.updateAtIndex(50, "Test2", 6)
    except IndexError:
        print("index 50 does not exist!")
    try:
        print(f"update student at index 10 with name Test3 and grade -6")
        repo.updateAtIndex(10, "Test3", -6)
    except ValueError:
        print("grade is not correct! Only name is updated")
        print(f"now the student at index 10 is {repo[10]}")

    print("ex.10.")
    print(repo)
    print(f"update student by ID 6 with name Test4 and grade 4")
    repo.updateByID(6, "Test4", 4)
    print(f"now the student with ID 6 is {repo.getByID(6)}")
    try:
        print(f"update student bu ID 50 with name Test5 and grade 6")
        repo.updateByID(50, "Test5", 6)
    except IndexError:
        print("ID 50 does not exist!")
    try:
        print(f"update student with ID 10 with name Test6 and grade -6")
        repo.updateByID(10, "Test6", -6)
    except ValueError:
        print("grade is not correct! Only name is updated")
        print(f"now the student with ID 10 is {repo.getByID(10)}")

    print("ex.11.")
    print(repo)
    print(f"number of students in the repository is {repo.getStudentCount()}")
    print(f"delete student at index 4")
    repo.deleteAtIndex(4)
    print(f"now the student at index 4 is {repo[4]}")
    print(f"number of students in the repository is {repo.getStudentCount()}")
    try:
        print(f"delete student at index 50")
        repo.deleteAtIndex(50)
    except IndexError:
        print("index 50 does not exist!")
        print(f"number of students in the repository is {repo.getStudentCount()}")

    print("ex.12.")
    print(repo)
    print(f"delete student by ID 6")
    repo.deleteByID(6)
    print(f"number of students in the repository is {repo.getStudentCount()}")
    print(repo)
    try:
        print(f"delete student bu ID 6")
        repo.deleteByID(6)
    except IndexError:
        print("ID 6 does not exist!")
        print(f"number of students in the repository is {repo.getStudentCount()}")


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
    print(" 6 - get student at index")
    print(" 7 - get student by ID")
    print(" 8 - get students with grade less than")
    print(" 9 - update student at index")
    print("10 - update student by ID")
    print("11 - delete student at index")
    print("12 - delete student by ID")


def start():
    print()
    studRepo = s.StudentRepository()
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
                    studRepo.addStudent(id_, name, grade)
                    print(studRepo)
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                index = int(input("Index of the student: "))
                id_ = int(input("Id of the student: "))
                name = input("Name of the student: ")
                grade = int(input("Grade of the student: "))
                try:
                    studRepo.insertStudent(index, id_, name, grade)
                    print(studRepo)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
            elif command == 3:
                print(f"Number of students in the list: {studRepo.getStudentCount()}")
            elif command == 4:
                id_ = int(input("Id of the student: "))
                print(f"Index of the student by the specific id {id_}: {studRepo.getIndexOfStudent(id_)}")
            elif command == 5:
                print(studRepo.getStudents())
            elif command == 6:
                index = int(input("Index:"))
                try:
                    print(f"The student at index {index} is {studRepo[index]}")
                except IndexError as ie:
                    print(ie)
            elif command == 7:
                id_ = int(input("ID:"))
                try:
                    print(f"The student with ID {id_} is {studRepo.getByID(id_)}")
                except IndexError as ie:
                    print(ie)
            elif command == 8:
                maxGrade = int(input("Maximum grade: "))
                print(f"Students with grade less than {maxGrade} are: {studRepo.getStudentsGradeLess(maxGrade)}")
            elif command == 9:
                index = int(input("Index:"))
                name = input("New name: ")
                grade = int(input("New grade: "))
                try:
                    originalStudent = studRepo[index]
                    studRepo.updateAtIndex(index, name, grade)
                    print(f"The student at index {index} was updated.")
                    print(f"Before update:\t{originalStudent}")
                    print(f"After update:\t{studRepo[index]}")
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)
            elif command == 10:
                id_ = int(input("ID:"))
                name = input("New name: ")
                grade = int(input("New grade: "))
                try:
                    originalStudent = studRepo.getByID(id_)
                    studRepo.updateByID(id_, name, grade)
                    print(f"The student with ID {id_} was updated.")
                    print(f"Before update:\t{originalStudent}")
                    print(f"After update:\t{studRepo.getByID(id_)}")
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)
            elif command == 11:
                index = int(input("Index:"))
                try:
                    studRepo.deleteAtIndex(index)
                    print(f"The student at index {index} is")
                except IndexError as ie:
                    print(ie)
            elif command == 12:
                id_ = int(input("ID:"))
                try:
                    studRepo.deleteByID(id_)
                    print(f"The student with ID {id_} was deleted")
                except IndexError as ie:
                    print(ie)
                    print(f"Can not find student with ID {id_}")
            else:
                print("invalid command")
        except ValueError:
            print("invalid type entered!")


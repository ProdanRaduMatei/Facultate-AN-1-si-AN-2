from unittest import TestCase
from domain import students as s


class StudentTestClass(TestCase):
    def setUp(self):
        self.student = s.Student(1, "A", "813", [9, 5, 7])
        self.studentWithoutGrade = s.Student(2, "B", "812", [])

    def testCreateStudent(self):
        self.assertEqual(self.student.name, "A")
        self.assertEqual(self.student.id, 1)
        self.assertEqual(self.student.group, "813")
        self.assertEqual(self.student.grades, [9, 5, 7])
        # it will call the following function
        # s.Student(2, "B", "813", [-1])
        self.assertRaises(ValueError, s.Student, 2, "B", "813", [-1])

    def testSetName(self):
        self.student.name = "B"
        self.assertEqual(self.student.name, "B")

    def testSetId(self):
        self.student.id = 5
        self.assertEqual(self.student.id, 5)

    def testSetGroup(self):
        self.student.group = "811"
        self.assertEqual(self.student.group, "811")

    def testStringRepresentation(self):
        self.assertEqual(str(self.student), "Student(1, A, 813, [9, 5, 7])")

    def testMaximumGrade(self):
        self.assertEqual(self.student.maximumGrade(), 9)
        self.assertIsNone(self.studentWithoutGrade.maximumGrade())

    def testMinimumGrade(self):
        self.assertEqual(self.student.minimumGrade(), 5)
        self.assertIsNone(self.studentWithoutGrade.minimumGrade())

    def testAverageGrade(self):
        self.assertEqual(self.student.averageGrade(), 7)
        self.assertIsNone(self.studentWithoutGrade.averageGrade())


class StudentRepositoryTestClass(TestCase):
    def setUp(self):
        self.emptyRepository = s.StudentRepository()
        self.repository1 = s.StudentRepository([
            s.Student(1, "A", "811", [5, 9, 6]),
            s.Student(2, "B", "811", [8]),
            s.Student(3, "C", "813", [9, 7]),
            s.Student(4, "D", "813", []),
            s.Student(5, "E", "812", [4, 6]),
        ])
        self.repository2 = s.StudentRepository([
            s.Student(11, "K", "811", []),
            s.Student(12, "L", "811", [8]),
            s.Student(13, "M", "813", [8, 6]),
            s.Student(14, "K", "813", [5]),
            s.Student(15, "O", "812", [4, 8]),
            s.Student(16, "P", "812", [8, 7, 6]),
            s.Student(17, "Q", "812", [7]),
        ])

    def testCreateStudentRepository(self):
        self.assertEqual(self.emptyRepository.getStudentCount(), 0)
        self.assertEqual(self.repository1.getStudentCount(), 5)
        self.assertEqual(self.repository2.getStudentCount(), 7)
        self.assertRaises(
                ValueError,
                s.StudentRepository,
                [s.Student(1, "", "", []), s.Student(1, "", "", [])]
        )

    def testGetMaximumGrade(self):
        self.assertRaises(ValueError, self.emptyRepository.getMaximumGrade)
        self.assertEqual(self.repository1.getMaximumGrade(), 9)
        self.assertEqual(self.repository2.getMaximumGrade(), 8)

    def testGetStudentsWithMaximumGrades(self):
        self.assertIsInstance(self.repository1.getStudentsWithMaximumGrades(), s.StudentRepository)
        self.assertEqual(self.repository1.getStudentsWithMaximumGrades(),
                         s.StudentRepository([
                             s.Student(1, "A", "811", [5, 9, 6]),
                             s.Student(3, "C", "813", [9, 7])
                         ]))
        self.assertEqual(self.repository2.getStudentsWithMaximumGrades(),
                         s.StudentRepository([
                             s.Student(12, "L", "811", [8]),
                             s.Student(13, "M", "813", [8, 6]),
                             s.Student(15, "O", "812", [4, 8]),
                             s.Student(16, "P", "812", [8, 7, 6])
                         ]))

    def testGetMaximumAverageGrade(self):
        self.assertRaises(ValueError, self.emptyRepository.getMaximumAverageGrade)
        self.assertEqual(self.repository1.getMaximumAverageGrade(), 8.0)
        self.assertEqual(self.repository2.getMaximumAverageGrade(), 8.0)

    def testGetStudentsWithMaximumAverageGrades(self):
        self.assertIsInstance(self.repository1.getStudentsWithMaximumAverageGrades(), s.StudentRepository)
        self.assertEqual(self.repository1.getStudentsWithMaximumAverageGrades(),
                         s.StudentRepository([
                             s.Student(2, "B", "811", [8]),
                             s.Student(3, "C", "813", [9, 7])
                         ]))
        self.assertEqual(self.repository2.getStudentsWithMaximumAverageGrades(),
                         s.StudentRepository([
                             s.Student(12, "L", "811", [8]),
                         ]))

    def testGetAverageOfMaximumsInGroup(self):
        for group in ["811", "812", "813"]:
            self.assertRaises(ValueError, self.emptyRepository.getAverageOfMaximumsInGroup, group)

        self.assertEqual(self.repository1.getAverageOfMaximumsInGroup("811"), 8.5)
        self.assertEqual(self.repository1.getAverageOfMaximumsInGroup("812"), 6.0)
        self.assertEqual(self.repository1.getAverageOfMaximumsInGroup("813"), 9.0)
        self.assertRaises(ValueError, self.repository1.getAverageOfMaximumsInGroup, "814")

        self.assertEqual(self.repository2.getAverageOfMaximumsInGroup("811"), 8.0)
        # delta: number of digits after the decimal which will be compared
        self.assertAlmostEqual(self.repository2.getAverageOfMaximumsInGroup("812"), 7.66, delta=1e-2)
        self.assertEqual(self.repository2.getAverageOfMaximumsInGroup("813"), 6.5)
        self.assertRaises(ValueError, self.repository2.getAverageOfMaximumsInGroup, "814")

    def testGetMinimumGradeInGroup(self):
        for group in ["811", "812", "813"]:
            self.assertRaises(ValueError, self.emptyRepository.getMinimumGradeInGroup, group)

        self.assertEqual(self.repository1.getMinimumGradeInGroup("811"), 5)
        self.assertEqual(self.repository1.getMinimumGradeInGroup("812"), 4)
        self.assertEqual(self.repository1.getMinimumGradeInGroup("813"), 7)
        self.assertRaises(ValueError, self.repository1.getMinimumGradeInGroup, "814")

        self.assertEqual(self.repository2.getMinimumGradeInGroup("811"), 8)
        # delta: number of digits after the decimal which will be compared
        self.assertEqual(self.repository2.getMinimumGradeInGroup("812"), 4)
        self.assertEqual(self.repository2.getMinimumGradeInGroup("813"), 5)
        self.assertRaises(ValueError, self.repository2.getMinimumGradeInGroup, "814")

    def testGetStudentIDsByName(self):
        self.assertEqual(self.emptyRepository.getStudentIDsByName("A"), [])
        self.assertEqual(self.repository1.getStudentIDsByName("A"), [1])
        self.assertEqual(self.repository2.getStudentIDsByName("K"), [11, 14])

    def testUpdateGroupOfStudent(self):
        self.repository1.updateGroupOfStudent(1, "511")
        self.assertEqual(self.repository1.getByID(1).group, "511")

        self.assertRaises(IndexError, self.emptyRepository.updateGroupOfStudent, 1, "813")

    def testDeleteGradesOfStudent(self):
        self.repository1.deleteGradesOfStudent(1)
        self.assertListEqual(self.repository1.getByID(1).grades, [])

        self.assertRaises(IndexError, self.emptyRepository.deleteGradesOfStudent, 3)

    def testDeleteStudentsFromGroup(self):
        self.repository1.deleteStudentsFromGroup("811")
        self.assertEqual(self.repository1.getStudentCount(), 3)
        self.repository1.deleteStudentsFromGroup("812")
        self.assertEqual(self.repository1.getStudentCount(), 2)
        self.repository1.deleteStudentsFromGroup("511")
        self.assertEqual(self.repository1.getStudentCount(), 2)
        self.repository1.deleteStudentsFromGroup("813")
        self.assertEqual(self.repository1.getStudentCount(), 0)

    def testDeleteStudentsWithNoGrades(self):
        self.repository1.deleteStudentsWithNoGrades()
        self.assertEqual(self.repository1.getStudentCount(), 4)
        self.emptyRepository.deleteStudentsWithNoGrades()
        self.assertEqual(self.emptyRepository.getStudentCount(), 0)

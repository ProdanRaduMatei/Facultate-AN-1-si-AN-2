def maximumGrade(students):
    """
    Get the maximum grade of all students.
    :param students: list of students
    :type students: list
    :return: maximum grade
    :rtype: int
    """
    maximum = 0
    for i in students:
        if i[1] > maximum:
            maximum = i[1]
    return maximum


def isPalindrome(value):
    """
    Defines if a string is palindrome or not.
    :param value:
    :type value: str
    :return:
    :rtype: bool
    """
    for i in range(len(value)//2):
        if(value[i] != value[-i-1]):
            return False
    return True
# return value == value[::-1]

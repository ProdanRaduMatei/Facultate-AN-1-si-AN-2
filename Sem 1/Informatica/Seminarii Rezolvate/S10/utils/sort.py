def bubbleSort(listOfValues):
    """
    seminar 10. ii. 1.
    Sorting the values of a given list in ascending order using bubble sort
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    pass


def minimumSelectionSort(listOfValues):
    """
    seminar 10. ii. 2.
    Sorting the values of a given list in ascending order using minimum selection sort
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    pass


def maximumSelectionSort(listOfValues):
    """
    seminar 10. ii. 2.
    Sorting the values of a given list in ascending order using maximum selection sort.
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    pass


def insertionSort(listOfValues):
    """
    seminar 10. ii. 3
    Sorting the values of a given list in ascending order using insertion sort.
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    pass


def splitList(listOfValues):
    """
    Splitting the list in two for the quick sort.
    :param listOfValues:
    :return: the position of the first element
    """
    pass


def recursiveQuickSort(listOfValues, startIndex=None, endIndex=None):
    """
    Recursively ordering the list with quick sort algorithm.
    :param listOfValues:
    :param startIndex:
    :type: int
    :param endIndex:
    :type: int
    :return: the ordered list
    :rtype: list
    """
    pass


def iterativeQuickSort(listOfValues):
    """
    seminar 10. ii. 4
    Sorting the values of a given list in ascending order using quick sort.
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    pass


def mySort(listOfValues, condition):
    """
    Sorting the values of a given list based on a given condition using bubble sort.
    :param listOfValues:
    :param condition: function having two parameters defining the correct relation between two elements in the list
    :type: callable (a reference to a function or a lambda expression)
    :return: ordered list
    :rtype: list
    """
    pass


def inBuiltSort(listOfValues, condition):
    """
    Sorting the values of a given list based on a given condition using insertion sort.
    :param listOfValues:
    :param condition: function having two parameters defining the correct relation between two elements in the list
    :type: callable (a reference to a function or a lambda expression)
    :return: ordered list
    :rtype: list
    """
    return sorted(listOfValues, key=condition)

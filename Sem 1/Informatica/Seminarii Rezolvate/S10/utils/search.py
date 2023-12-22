def sequentialSearchUnordered(listOfValues, searchedValue):
    """
    seminar 9. ii. 1.
    Searching for a given value in an unordered list using sequential search.
    :param listOfValues:
    :param searchedValue:
    :return: first position of the searched element
    :rtype: int
    """
    for index, x in enumerate(listOfValues):
        if x == searchedValue:
            return index
    return -1


def sequentialSearchOrdered(listOfValues, searchedValue):
    """
    seminar 9. ii. 1.
    Searching for a given value in an ordered list using sequential search.
    :param listOfValues:
    :param searchedValue:
    :return: first position of the searched element
    :rtype: int
    """
    for index, x in enumerate(listOfValues):
        if x == searchedValue:
            return index
        if x > searchedValue:
            break
    return -1


def binarySearch(listOfValues, searchedValue, startIndex=None, endIndex=None):
    """
    seminar 9. ii. 2.
    Searching for a given value in an ordered list using binary search.
    :param listOfValues:
    :param searchedValue:
    :param startIndex:
    :param endIndex:
    :return: first position of the searched element
    :rtype: int
    """
    if startIndex is None:
        startIndex = 0
    if endIndex is None:
        endIndex = len(listOfValues) - 1
    if startIndex >= endIndex:
        return -1
    else:
        middle = (startIndex + endIndex) // 2
        if listOfValues[middle] == searchedValue:
            return middle
        if listOfValues[middle] < searchedValue:
            return binarySearch(listOfValues, searchedValue, middle + 1, endIndex)
        else:
            return binarySearch(listOfValues, searchedValue, 0, middle - 1)


def myFilter(listOfValues, criterion):
    """
    Filter elements of the list based on the given condition
    :param listOfValues:
    :param criterion: function having one parameter defining the condition of inclusion of a value in the result list
    :type: callable (a reference to a function or a lambda expression)
    :return: the filtered list
    :rtype: list
    """
    result=[]
    # result=list()
    for value in listOfValues:
        if criterion(value):
            result.append(value)
    return result


def inBuiltFilter(listOfValues, criterion):
    """
    Filter elements of the list based on the given condition using Python's in-built function
    :param listOfValues:
    :param criterion: function having one parameter defining the condition of inclusion of a value in the result list
    :type: callable (a reference to a function or a lambda expression)
    :return: the filtered list
    :rtype: list
    """
    return list(filter(criterion, listOfValues))

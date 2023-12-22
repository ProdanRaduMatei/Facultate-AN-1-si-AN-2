def bubbleSort(listOfValues):
    """
    seminar 10. ii. 1.
    Sorting the values of a given list in ascending order using bubble sort
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    ordered = False
    onFinalPosition = 0
    while not ordered:
        ordered = True
        for i in range(len(listOfValues) - onFinalPosition - 1):
            if listOfValues[i] > listOfValues[i + 1]:
                # listOfValues[i], listOfValues[i + 1] = listOfValues[i + 1], listOfValues[i]
                aux = listOfValues[i]
                listOfValues[i] = listOfValues[i + 1]
                listOfValues[i + 1] = aux
                ordered = False
        onFinalPosition += 1
    return listOfValues


def insertionSort(listOfValues):
    """
    seminar 10. ii. 3
    Sorting the values of a given list in ascending order using insertion sort.
    - get the first element of the unordered part
    - search its position in the ordered part
    - insert it
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    for i in range(len(listOfValues) - 1):
        tmp = listOfValues[i]
        j = i - 1
        while j >= 0 and tmp < listOfValues[j]:
            listOfValues[j + 1] = listOfValues[j]
            j -= 1
        listOfValues[j + 1] = tmp


def minimumSelectionSort(listOfValues):
    """
    seminar 10. ii. 2.
    Sorting the values of a given list in ascending order using minimum selection sort
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    for i in range(len(listOfValues)-1):
        min = listOfValues[i]
        position = i
        for j in range(i+1,len(listOfValues)):
            if listOfValues[j] < min:
                min = listOfValues[j]
                position = j
        listOfValues[i], listOfValues[position] = listOfValues[position], listOfValues[i]
    return listOfValues


def maximumSelectionSort(listOfValues):
    """
    seminar 10. ii. 2.
    Sorting the values of a given list in ascending order using maximum selection sort
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    for i in range(len(listOfValues)-1):
        currentMax = listOfValues[i]
        position = i
        for j in range(0,len(listOfValues)-i-1):
            if listOfValues[j] > currentMax:
                currentMax = listOfValues[j]
                position = j
        listOfValues[len(listOfValues)-i-1], listOfValues[position] = listOfValues[position], listOfValues[len(listOfValues)-i-1]
    return listOfValues


def splitList(listOfValues):
    """
    Splitting the list in two for the quick sort
    :param listOfValues:
    :return: the position of the first element
    """
    middle, left, right = 0, 1, len(listOfValues) - 1
    while left < right:
        if (listOfValues[left] >= listOfValues[middle] and listOfValues[right] <= listOfValues[middle]):
            listOfValues[left], listOfValues[right] = listOfValues[right], listOfValues[left]
            left += 1
            right -=1
        elif listOfValues[left] <= listOfValues[middle] and listOfValues[right] <= listOfValues[middle]:
            left +=1
        else:
            right -=1
    return left


def splitList2(listOfValues):
    """
    Splitting the list in two for the quick sort
    :param listOfValues:
    :return: the position of the first element
    """
    left, right = 0, len(listOfValues) - 1
    stepLeft, stepRight = 0, -1
    while left < right:
        if listOfValues[left] > listOfValues[right]:
            listOfValues[left], listOfValues[right] = listOfValues[right], listOfValues[left]
            stepLeft, stepRight = stepRight * (-1), stepLeft * (-1)
        left += stepLeft
        right += stepRight
    return left


def recursiveQuickSort(listOfValues):
    """
    Recursively ordering the list with quick sort algorithm
    :param listOfValues:
    :param startIndex:
    :type: int
    :param endIndex:
    :type: int
    :return: the ordered list
    :rtype: list
    """
    if len(listOfValues) < 2:
        return listOfValues
    middle = splitList2(listOfValues)
    return recursiveQuickSort(listOfValues[:middle]) + [listOfValues[middle]] + recursiveQuickSort(listOfValues[middle + 1:])


# def recursiveQuickSort(listOfValues):
#     """
#     Recursively ordering the list with quick sort algorithm
#     :param listOfValues:
#     :param startIndex:
#     :type: int
#     :param endIndex:
#     :type: int
#     :return: the ordered list
#     :rtype: list
#     """
#     if len(listOfValues) < 2:
#         return listOfValues
#     middle = splitList(listOfValues)
#     print(f"{listOfValues[0] = }")
#     print(f"{listOfValues[1:middle] = }")
#     print(f"{listOfValues[middle:] = }")
#     return recursiveQuickSort(listOfValues[1:middle]) + [listOfValues[0]] + recursiveQuickSort(listOfValues[middle:])


def iterativeQuickSort(listOfValues):
    """
    seminar 10. ii. 4
    Sorting the values of a given list in ascending order using quick sort
    :param listOfValues:
    :return: ordered list
    :rtype: list
    """
    pass


def mySort(listOfValues, condition):
    """
    Sorting the values of a given list based on a given condition using bubble sort
    :param listOfValues:
    :param condition: function having two parameters defining the correct relation between two elements in the list
    :type: callable (a reference to a function or a lambda expression)
    :return: ordered list
    :rtype: list
    """
    ordered = False
    onFinalPosition = 0
    while not ordered:
        ordered = True
        for i in range(len(listOfValues) - onFinalPosition - 1):
            if not condition(listOfValues[i], listOfValues[i + 1]):
                # listOfValues[i], listOfValues[i + 1] = listOfValues[i + 1], listOfValues[i]
                aux = listOfValues[i]
                listOfValues[i] = listOfValues[i + 1]
                listOfValues[i + 1] = aux
                ordered = False
        onFinalPosition += 1
    return listOfValues


def inBuiltSort(listOfValues, condition):
    """
    Sorting the values of a given list based on a given condition using insertion sort
    :param listOfValues:
    :param condition: function having two parameters defining the correct relation between two elements in the list
    :type: callable (a reference to a function or a lambda expression)
    :return: ordered list
    :rtype: list
    """
    return sorted(listOfValues, key=condition)

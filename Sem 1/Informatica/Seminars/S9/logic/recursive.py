def factorial(n):
    """
    ex. 1.
    Calculating the factorial of a given number.
    defined for n >= 1
    1! = 1
    n! = 1 * 2 * ... * n
    n! = n * (n - 1)!
    :param n: given number
    :type n: int
    :return: factorial of the number
    :rtype: int
    """
    if n < 1:
        raise ValueError("Factorial of n < 1 can not be calculated!")
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """
    ex. 2.
    Calculating the n-th element from the Fibonacci sequence.
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
    :param n: index of the element in the Fibonacci sequence
    :type n: integer
    :return: n-th element from the Fibonacci sequence
    :rtype: integer
    """
    if n<0:
        raise ValueError()
    elif n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def multiplication(n):
    """
    ex. 3.
    Calculating the value of function f(n) = 3 * n
    f(0) = 0
    f(n) = 3 + 3 + ... + 3 (n times)
    f(n) = 3 + f(n - 1)
    :param number: given number
    :type number: int
    :return: value of the function f in n
    :rtype: int
    """
    if n<0:
        raise ValueError()
    if(n==0):
        return 0
    return 3+ multiplication(n-1)


def sum(n):
    """
    ex. 4.
    Calculating the sum of first n integers.
    sum(0) = 0
    sum(n) = 1 + 2 + ... + n
    sum(n) = n + sum(n - 1)
    :param n: given number
    :type n: int
    :return: sum of numbers till n
    :rtype: int
    """
    if n < 0:
        return
    elif n == 0:
        return 0
    else:
        return n + sum(n-1)


def pascal(n):
    """
    ex. 5.
    Calculating the n-th row of Pascal's triangle.
    1
    1 1
    1 2 1
    1 3 3 1
    :param n: number of the row
    :type n: int
    :return: the n-th row of Pascal's triangle
    :rtype: list
    """
    if n < 1:
        return None
    if n == 1:
        return [1]
    else:
        prev_row = pascal(n-1)
        current_row = [1]
        for i in range(len(prev_row)-1):
            current_row.append(prev_row[i] + prev_row[i+1])
        # for i in range(1, len(prev_row)):
        #     current_row.append(prev_row[i] + prev_row[i-1])
        current_row.append(1)
        return current_row


def minimum(listOfValues):
    """
    ex. 6.a.
    Calculating the minimum value of a list.
    :param listOfValues: list of number
    :type listOfValues: list
    :return: the minimum value of a list
    :rtype: int
    """
    if len(listOfValues) == 0:
        return None
    if len(listOfValues) == 1:
        return listOfValues[0]
    else:
        return min(listOfValues[0], minimum(listOfValues[1:]))


def maximum(listOfValues):
    """
    ex. 6.b.
    Calculating the maximum of a list
    :param listOfValues: list of number
    :type listOfValues: list
    :return: the maximum value of a list
    :rtype: int
    """
    if len(listOfValues) == 0:
        return None
    if len(listOfValues) == 1:
        return listOfValues[0]
    else:
        return max(listOfValues[0], maximum(listOfValues[1:]))


def recursiveMin(listOfValues):
    """
    ex. 7.
    Calculating the minimum value of a nested list.
    :param listOfValues: nested list of numbers
    :type listOfValues: list
    :return: minimum of the nested list
    :rtype: int
    """
    if len(listOfValues) == 0:
        return
    if len(listOfValues) == 1:
        if type(listOfValues[0]) == list:
            return recursiveMin(listOfValues[0])
        else:
            return listOfValues[0]
    else:
        if type(listOfValues[0]) == list:
            min_first = recursiveMin(listOfValues[0])
        else:
            min_first = listOfValues[0]
        min_rest = recursiveMin(listOfValues[1:])
        if min_first is None:
            return min_rest
        if min_rest is None:
            return min_first
        else:
            return min(min_first, min_rest)


def count(value, listOfValues):
    """
    ex. 8.
    Calculating the occurence of value in a nested list
    :param value: value to search
    :type value: int
    :param listOfValues: list of numbers
    :type listOfValues: list
    :return: occurence of value in the list
    :rtype: int
    """
    if len(listOfValues) == 0:
        return 0
    if listOfValues[0] == value:
        return 1 + count(value, listOfValues[1:])
    elif type(listOfValues[0]) == list:
        return count(value, listOfValues[0]) + count(value, listOfValues[1:])
    else:
        return count(value, listOfValues[1:])

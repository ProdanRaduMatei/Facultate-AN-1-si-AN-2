# lambda value: value % 2 == 0
def isEven(value):
    """
    Defines if a given number is even
    :param value: given number
    :type: int
    :return: if the number is even
    :rtype: bool
    """
    return value % 2 == 0


def isArmstrong(value):
    """
    Defines if a given number is Armstrong number
    :param value: given number
    :type: int
    :return: if the number is Armstrong number
    :rtype: bool
    """
    s = 0
    c = value
    while value > 0:
        s += (value % 10) ** 3
        value //= 10
    return s == c


def isPrime(value):
    """
    Defines if a given number is prime
    :param value: given number
    :type: int
    :return: if the number is prime
    :rtype: bool
    """
    if value < 2:
        return False
    else:
        for number in range(2, value // 2):
            if value % number == 0:
                return False
        return True


def isPerfectSquare(value):
    """
    Defines if the given number is a perfect square
    :param value: given number
    :type: int
    :return: if the number is perfect square
    :rtype: bool
    """
    nr = 2
    if 0 <= value < 2:
        return True
    while nr <= value / 2:
        if nr * nr == value:
            return True
        nr += 1
    return False


# lambda value: isArmstrong(value) and isEven(value)
def criterion_i_2(value):
    """
    Defines if a given number is Armstrong number and even.
    :param value: given number
    :type: int
    :return: if the number is Armstrong number and even
    :rtype: bool
    """
    return isArmstrong(value) and isEven(value)


# lambda value: is_armstrong(value) or is_even(value) or is_prime(value) or is_prefect_square(value)
def criterion_i_3(value):
    """
    Defines if a given number is Armstrong number and even.
    :param value: given number
    :type: int
    :return: if the number is Armstrong number and even
    :rtype: bool
    """
    return isArmstrong(value) or isEven(value) or isPrime(value) or isPerfectSquare(value)

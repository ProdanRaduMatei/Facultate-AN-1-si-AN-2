def init():
    """
    Initialize the next element of the solution
    :returns: initial value of the last element of the solution
    :rtype: int
    """
    return -1


def nextElement(solution, position):
    """
    Get the next possible element of the solution
    :param solution: list containing the solution
    :type solution: list
    :param position: position of the element for which the next element should be defined
    :type position: int
    :returns: next possible element for the given position
    :rtype: int
    """
    return solution[position] + 1


def generateRecursiveSolutions(solution, initElementFn, nextElementFn, doesElementExistFn, isConsistentFn,
                               isSolutionFn):
    """
    Generate solutions for a given program with recursive solution
    :param solution: current state of the solution
    :type solution: list
    :param initElementFn: function to initialize the next element of the solution
    :type initElementFn: Callable
    :param nextElementFn: gets the next value for the last element of the solution
    :type nextElementFn: Callable
    :param doesElementExistFn: checks if the value of the last element (of the solution) is correct
    :type doesElementExistFn: Callable
    :param isConsistentFn: checks if the current solution is consistent
    :type isConsistentFn: Callable
    :param isSolutionFn: checks if the current content of the solution is a final solution
    :type isSolutionFn: Callable
    :returns: a final solution
    :rtype: list
    """
    solution.append(init())
    # nextElement = nextElementFn(solution, len(solution) - 1)
    nextElementValue = nextElementFn(solution, -1)
    while doesElementExistFn(nextElementValue):
        solution[-1] = nextElementValue
        if isConsistentFn(solution):
            if isSolutionFn(solution):
                yield solution[:]
            else:
                yield from generateRecursiveSolutions(solution[:], initElementFn,
                                                      nextElementFn, doesElementExistFn,
                                                      isConsistentFn, isSolutionFn)
        nextElementValue = nextElementFn(solution, -1)


def generateIterativeSolutions(initElementFn, nextElementFn, doesElementExistFn, isConsistentFn, isSolutionFn):
    """
    Generate solutions for a given program with iterative solution
    :param initElementFn: function to initialize the next element of the solution
    :type initElementFn: Callable
    :param nextElementFn: gets the next value for the last element of the solution
    :type nextElementFn: Callable
    :param doesElementExistFn: checks if the value of the last element (of the solution) is correct
    :type doesElementExistFn: Callable
    :param isConsistentFn: checks if the current solution is consistent
    :type isConsistentFn: Callable
    :param isSolutionFn: checks if the current content of the solution is a final solution
    :type isSolutionFn: Callable
    :returns: a final solution
    :rtype: list
    """
    k = 0
    solution = [initElementFn()]
    while k >= 0:
        solution[-1] = nextElementFn(solution, -1)
        if doesElementExistFn(solution[-1]):
            if isConsistentFn(solution):
                if isSolutionFn(solution):
                    yield solution[:]
                else:
                    k += 1
                    solution.append(initElementFn())
        else:
            k -= 1
            del solution[-1]


def getSolutions(listOfValues, initElementFn=init, nextElementFn=nextElement, doesElementExistFn=lambda element: False,
                 isConsistentFn=lambda solution: False, isSolutionFn=lambda solution: False, iterative=False):
    if iterative:
        fn = generateIterativeSolutions
        args = []
    else:
        fn = generateRecursiveSolutions
        args = [[]]
    return [list(map(lambda index: listOfValues[index], solution)) for solution in
            fn(*args, initElementFn, nextElementFn, doesElementExistFn, isConsistentFn,
               isSolutionFn)]

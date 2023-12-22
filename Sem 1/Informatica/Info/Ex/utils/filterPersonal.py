def searchBy(l, condition):

    result = []
    for item in l:
        if condition(item):
            result.append(item)
    return result[:]

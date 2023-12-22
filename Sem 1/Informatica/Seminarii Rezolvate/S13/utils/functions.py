def bubble_sort(lst, condition):
    """
    Sort a given list using the specified condition.
    :param lst:
    :type lst: list
    :param condition:
    :type condition: callable
    :return:
    :rtype:
    """
    ok = 0
    while ok == 0:
        ok = 1
        for i in range(0, len(lst) - 1):
            if condition(lst[i], lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                ok = 0

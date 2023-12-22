from domain.object import Object
from utils.functions import bubble_sort


class Store:
    def __init__(self, listOfObjects=None):
        self.__listOfObjects = []

        if listOfObjects is not None:
            for obj in listOfObjects:
                if isinstance(obj, Object):
                    self.__listOfObjects.append(obj)

    def lengthListOfObj(self):
        """
        Get number of items in the store
        :return:
        :rtype:
        """
        return len(self.__listOfObjects)

    def __getitem__(self, item):
        """
        Get element at given position from the store
        :param item:
        :type item:
        :return:
        :rtype:
        """
        return self.__listOfObjects[item]

    def __repr__(self):
        """
        Get a string representation of the object
        :return:
        :rtype:
        """
        return str(self.__listOfObjects)

    def sort(self):
        """
        Sort the items in the store first by wight and then by value
        :return:
        :rtype:
        """
        bubble_sort(self.__listOfObjects, lambda x, y: x.weight > y.weight)
        bubble_sort(self.__listOfObjects, lambda x, y: x.value < y.value)

class Backpack:
    def __init__(self, maxWeight):
        self.__maxWeight = maxWeight

        self.__stolenItems = []

    @property
    def currentWeight(self):
        """
        Get the weight packed to the backpack
        :return:
        :rtype:
        """
        return sum(map(lambda item: item.weight, self.__stolenItems))

    @property
    def currentValue(self):
        """
        Get the value of the items packed in the backpack
        :return:
        :rtype:
        """
        return sum(map(lambda item: item.value, self.__stolenItems))

    def put(self, item):
        """
        Put an item into the backpack
        :param item:
        :type item:
        :raise ValueError: if the item does not fit
        :return:
        :rtype:
        """
        if self.currentWeight + item.weight > self.__maxWeight:
            raise ValueError("Object can not be put into the backpack!")
        self.__stolenItems.append(item)

    def __repr__(self):
        """
        Get a string representation of the backpack
        :return:
        :rtype:
        """
        return f"Value: {self.currentValue}\nItems: {self.__stolenItems}"

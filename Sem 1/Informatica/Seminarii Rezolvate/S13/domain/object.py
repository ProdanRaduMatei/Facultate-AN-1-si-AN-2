class Object:
    def __init__(self, v, w):
        self.__value = v
        self.__weight = w

    @property
    def value(self):
        """
        Get value of the object
        :return:
        :rtype:
        """
        return self.__value

    @property
    def weight(self):
        """
        Get weight of the object
        :return:
        :rtype:
        """
        return self.__weight

    def setValue(self, value):
        """
        Set value of the object
        :param value:
        :type value: float
        :return:
        :rtype:
        """
        self.__value = value

    def setWeight(self, weight):
        """
        Set weight of the object
        :param weight:
        :type weight: float
        :return:
        :rtype:
        """
        self.__weight = weight

    def __repr__(self):
        """
        Get a string representation of the object
        :return:
        :rtype:
        """
        return "Object(value=" + str(self.__value) + ", weight= " + str(self.__weight)

class GeometricalShape:
    __shape_names = {
        3: "triangle",
        4: "square",
        5: "pentagon",
        6: "hexagon",
        7: "heptagon",
        8: "octogon",
        9: "nonagon",
        10: "decagon",
        12: "dodecagon"
    }

    def __init__(self, sideLengths, name=None):
        if len(sideLengths) < 3:
            raise ValueError(f"A geometrical shape should have at least 3 sides, but {len(sideLengths)} given!")

        self.__numberOfSides = len(sideLengths)
        if name is None:
            self.__name = GeometricalShape.__shape_names.get(self.__numberOfSides,
                                                             f"polygon with {self.__numberOfSides} sides")
        else:
            self.__name = name
        self.__sideLengths = sideLengths[:]

    @property
    def numberOfSides(self):
        """
        Get number of sides of the polygon
        :returns: int
        """
        return self.__numberOfSides

    @property
    def name(self):
        """
        Get name of the polygon
        :returns: str
        """
        return self.__name

    @name.setter
    def name(self, newName):
        """
        Set name of the polygon
        :param newName: new name of the polygon
        :type newName: str
        """
        self.__name = newName

    @property
    def sideLengths(self):
        """
        Get length of each side of the polygon
        :returns: list
        """
        return self.__sideLengths[:]

    @sideLengths.setter
    def sideLengths(self, newLengths):
        """
        Set the length of each side of the polygon
        :param newLengths: new length of the sides
        :type newLengths: list
        """
        if len(newLengths) < 3:
            raise ValueError(f"A geometrical shape should have at least 3 sides, but {len(newLengths)} given!")

        self.__numberOfSides = len(newLengths)
        self.__sideLengths = newLengths[:]

    def perimeter(self):
        """
        Get the perimeter of the polygon
        :returns: int
        """
        return sum(self.__sideLengths)

    def __str__(self):
        """
        Converting the object into string
        :returns: str
        """
        return f"{self.__name} ({self.__numberOfSides}) {self.__sideLengths} (perimeter = {self.perimeter()})"


if __name__ == "__main__":
    g = GeometricalShape([1, 2, 3])
    print(g)

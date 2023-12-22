from infrastructure.repository import ShapeRepository


class ShapeController:
    def __init__(self, initialShapes=None):
        self.__shapeRepo = ShapeRepository(initialShapes)

    def __str__(self):
        """
        Converting the object into string.
        """
        return f"In controller:\n{self.__shapeRepo}"

    def add(self, sideLengths, name):
        """
        Add a new shape to the repository
        :param sideLengths: list of lengths of the sides
        :type sideLengths: list
        :param name: name of the shape
        :type name: str
        """
        self.__shapeRepo.add(sideLengths, name)

    def __getitem__(self, index):
        """
        Get shape at a specified position
        :param index: position of the shape
        :type index: int
        :raises IndexError: if the index is not correct
        :returns: GeometricalShape
        """
        return self.__shapeRepo[index]

    def update(self, index, newLengths, newName):
        """
        Update shape at a specified position
        :param index: position of the shape
        :type index: int
        :param newLengths: new length of the sides
        :type newLengths: list
        :param newName: new name of the polygon
        :type newName: str
        """
        self.__shapeRepo.update(index, newLengths, newName)

    def __delitem__(self, index):
        """
        Delete shape at a specified position
        :param index: position of the shape
        :type index: int
        :raises IndexError: if the index is not correct
        """
        del self.__shapeRepo[index]

    def more_than_k_sides(self, k):
        return self.__shapeRepo.more_than_k_sides(k)

    def more_than_k_sides_in_built(self, k):
        return self.__shapeRepo.more_than_k_sides_in_built(k)

    def higher_perimeter(self, min_perimeter, name_length):
        return self.__shapeRepo.higher_perimeter(min_perimeter, name_length)

    def higher_perimeter_in_built(self, min_perimeter, name_length):
        return self.__shapeRepo.higher_perimeter_in_built(min_perimeter, name_length)

    def sort_by_perimeter(self, desc=False):
        return self.__shapeRepo.sort_by_perimeter(desc)

    def sort_by_perimeter_in_built(self, desc=False):
        return self.__shapeRepo.sort_by_perimeter_in_built(desc)

    def sort_name_starting_by_perimeter(self, name_prefix, desc=False):
        return self.__shapeRepo.sort_name_starting_by_perimeter(name_prefix, desc)

    def sort_name_starting_by_perimeter_in_built(self, name_prefix, desc=False):
        return self.__shapeRepo.sort_name_starting_by_perimeter_in_built(name_prefix, desc)

import copy

from logic.domain import GeometricalShape

from utils.search import myFilter, inBuiltFilter
from utils.sort import mySort, inBuiltSort


class ShapeRepository:
    def __init__(self, initialShapes=None):
        if initialShapes is None:
            self.__shapes = []
        else:
            # check if there are correct values in initialShapes
            for shape in initialShapes:
                if not isinstance(shape, GeometricalShape):
                    raise ValueError(
                        f"The repository should contain GeometricalShape instances, but {type(shape)} given!")
            self.__shapes = copy.deepcopy(initialShapes)

    def __str__(self):
        """
        Converting the object into string.
        """
        if len(self.__shapes) == 0:
            return "The repository is empty"
        str_repr = "Shapes of the repository:\n"
        for shape in self.__shapes:
            str_repr += "\t" + str(shape) + "\n"
        return str_repr

    def add(self, sideLengths, name):
        """
        Add a new shape to the repository
        :param sideLengths: list of lengths of the sides
        :type sideLengths: list
        :param name: name of the shape
        :type name: str
        """
        if name == "":
            name = None
        self.__shapes.append(GeometricalShape(sideLengths, name))

    def __getitem__(self, index):
        """
        Get shape at a specified position
        :param index: position of the shape
        :type index: int
        :raises IndexError: if the index is not correct
        :returns: GeometricalShape
        """
        if 0 <= index < len(self.__shapes):
            return self.__shapes[index]
        raise IndexError(f"Index ({index}) is not correct in list of {len(self.__shapes)} length.")

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
        if 0 <= index < len(self.__shapes):
            self.__shapes[index].name = newName
            self.__shapes[index].sideLengths = newLengths
        raise IndexError(f"Index ({index}) is not correct in list of {len(self.__shapes)} length.")

    def __delitem__(self, index):
        """
        Delete shape at a specified position
        :param index: position of the shape
        :type index: int
        :raises IndexError: if the index is not correct
        """
        if 0 <= index < len(self.__shapes):
            del self.__shapes[index]
        raise IndexError(f"Index ({index}) is not correct in list of {len(self.__shapes)} length.")

    def more_than_k_sides(self, k):
        return ShapeRepository(myFilter(self.__shapes, lambda x: x.numberOfSides > k))

    def more_than_k_sides_in_built(self, k):
        return ShapeRepository(inBuiltFilter(self.__shapes, lambda x: x.numberOfSides > k))

    def higher_perimeter(self, min_perimeter, name_length):
        return ShapeRepository(
            myFilter(self.__shapes, lambda x: x.parameter() > min_perimeter and len(x.name) > name_length))

    def higher_perimeter_in_built(self, min_perimeter, name_length):
        return ShapeRepository(
            inBuiltFilter(self.__shapes, lambda x: x.parameter() > min_perimeter and len(x.name) > name_length))

    def sort_by_perimeter(self, desc=False):
        if desc:
            return ShapeRepository(mySort(self.__shapes, lambda x, y: x.perimeter() > y.pentirmeter()))
        else:
            return ShapeRepository(mySort(self.__shapes, lambda x, y: x.perimeter() < y.pentirmeter()))

    def sort_by_perimeter_in_built(self, desc=False):
        if desc:
            return ShapeRepository(inBuiltSort(self.__shapes, lambda x, y: x.perimeter() > y.pentirmeter()))
        else:
            return ShapeRepository(inBuiltSort(self.__shapes, lambda x, y: x.perimeter() < y.pentirmeter()))

    def sort_name_starting_by_perimeter(self, name_prefix, desc=False):
        filtered = ShapeRepository(myFilter(self.__shapes, lambda x: x.name.startswith(name_prefix)))
        return filtered.sort_by_perimeter(desc)

    def sort_name_starting_by_perimeter_in_built(self, name_prefix, desc=False):
        filtered = ShapeRepository(inBuiltFilter(self.__shapes, lambda x: x.name.startswith(name_prefix)))
        return filtered.sort_by_perimeter_in_built(desc)

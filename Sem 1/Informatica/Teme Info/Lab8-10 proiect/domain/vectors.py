import utils.helpers as h
import math
import matplotlib.pyplot as plt
import numpy as np


class MyVector:
    def __init__(self, name_id, colour, type, values):
        self.__name_id = name_id
        if h.checkColor(colour):
            self.__colour = colour
        else:
            raise ValueError("Colour isnt't correct!")
        if h.checkType(type):
            self.__type = type
        else:
            raise ValueError("Type isn't correct!")
        self.__values = values
    
    def getId(self):
        """
        Get the id of the vector
        :return:
        :rtype: int
        """
        return self.name_id
    
    @property
    def name_id(self):
        return self.name_id
    
    @property
    def colour(self):
        return self.colour
    
    @property
    def type(self):
        return self.type
    
    @property
    def values(self):
        return self.values
    
    def setName_ID(self, newName_ID):
        self.__name_id = newName_ID
    
    def setColour(self, newColour):
        if h.checkColour(newColour):
            self.__colour = newColour
        else:
            raise ValueError("Colour isn't correct!")
    
    def setType(self, newType):
        if newType >= 1:
            self.__type = newType
        else:
            raise ValueError("Type isn't correct!")
    
    def setValues(self, newValues):
        self.__values = newValues
    
    def __repr__(self):
        return f"MyVector({self.name_id}, {self.colour}, {self.type}, {self.values})"
    
    def str(self):
        return self.__repr__()
    
    def addScalar(self, vector, scalar):
        vector2 = np.add(vector, scalar)
        return vector2
    
    def addVectors(self, values1, values2):
        values3 = np.add(values1, values2)
        return values3
    
    def substractVectors(self, values1, values2):
        values3 = np.subtract(values1, values2)
        return values3
    
    def multiplyVectors(self, values1, values2):
        values3 = np.multiply(values1, values2)
        return values3
    
    def sumInVector(self, values):
        s = np.sum(values)
        return s
    
    def productInVector(self, values):
        p = np.prod(values)
        return p
    
    def averageInVector(self, values):
        average = np.average(values)
        return average

    def minimumOfVector(self, values):
        minim = np.min(values)
        return minim
    
    def maximumOfVector(self, values):
        maxim = np.max(values)
        return maxim

class VectorRepository:
    def __init__(self, initialVectors=None):
        """
        Creating a repository containing vectors
        """
        self.__listOfVectors = []
        if initialVectors is not None:
            # check if the ids are unique
            for vector in initialVectors:
                if isinstance(vector, MyVector) and self.__isIdUnique(vector.id):
                    self.__listOfVectors.append(vector)
                else:
                    raise ValueError("student is not correct")
                
    def addVector(self, name_id, colour, type, values):
        """
        Add a new vector to the repository
        :param name_id:
        :type name_id: int
        :param colour:
        :type colour: str
        :param type:
        :type type: int
        :param values:
        :type values: list
        """
        if self.__isIdUnique(name_id):
            self.__listOfVectors.append(MyVector(name_id, colour, type, values))
        else:
            raise ValueError("ID already exists in the repository!")
        
    def getVectors(self):
        """
        Get all vectors from the repository.
        Return a copy of the list! Otherwise, the user can change the content of the list.
        :return:
        :rtype: list
        """
        return self.__listOfVectors[:]
    
    def getAtIndex(self, index):
        """
        Get vector at a specified index.
        :param index:
        :type index: int
        :return:
        :rtype: MyVector
        """
        if self.__isIndexCorrect(index):
            return self.__listOfVectors[index]
        else:
            raise IndexError(f"Index is not correct!")
        
    def updateAtIndex(self, index, name_id, colour, type, values):
        """
        Update a vector at a given index
        :param index:
        :type index: int
        :param name_id:
        :type name: str
        :param colour:
        :type colour: str
        :param type:
        :type colour: int
        :param values:
        :type colour: list
        """
        if self.__isIndexCorrect(index):
            vector = self.getAtIndex(index)
            # only if you have a setter defined with annotation
            # @name.setter
            # def name(self, name):
            #   ...
            vector.name_id = name_id
            vector.colour = colour
            vector.type = type
            vector.values = values
        else:
            raise IndexError("Index is not correct!")
        
    def updateByID(self, name_id_old, name_id, colour, type, values):
        """
        Update a vector at a given index
        :param name_id_old:
        :type name_id_old: int
        :param name_id:
        :type name_id: int
        :param colour:
        :type colour: str
        :param type:
        :type type: int
        :param values:
        :type values: list
        """
        self.updateAtIndex(self.getIndexOfVector(name_id_old), name_id, colour, type, values)
        
    def deleteAtIndex(self, index):
        """
        Delete a vector at a given index
        :param index:
        :type index: int
        """
        if self.__isIndexCorrect(index):
            del self.__listOfVectors[index]
        else:
            raise IndexError("Index is not correct!")
        
    def deleteByID(self, id_):
        """
        Delete a student at a given index
        :param id_:
        :type id_: int
        """
        self.deleteAtIndex(self.getIndexOfVector(id_))
        
    def PlotInChart(self):
        """
        Delete a student at a given index
        :param id_:
        :type id_: int
        """ 
        circle = []
        square = []
        triangle = []
        diamond = []
        for vectors in self.__listOfVectors:
            if vectors.type == 1:
                circle.append(vectors.colour)
            elif vectors.type == 2:
                square.append(vectors.colour)
            elif vectors.type == 3:
                triangle.append(vectors.colour)
            else:
                diamond.append(vectors.colour)
        fig, ax = plt.subplots()
        ax.scatter(circle, square, triangle, diamond)
        plt.show()
        
    def __isIdUnique(self, id_):
        """
        Check if the given id is already in the list
        :param id_:
        :type id_: int
        :return:
        :rtype: bool
        """
        for vector in self.__listOfVectors:
            if vector.name_id == id_:
                return False
        return True
    
    def __isIndexCorrect(self, index):
        """
        Check if the index is correct in the list of vector
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__listOfVectors) or 0 == index == len(self.__listOfVectors)
    
    def getIndexOfVector(self, name_id):
        """
        Get the index of a vector identified by its id.
        :param id_:
        :type id_: int
        :return:
        :rtype: int
        """
        for index, vector in enumerate(self.__listOfVectors):
            if vector.getId() == name_id:
                return index
        return -1 
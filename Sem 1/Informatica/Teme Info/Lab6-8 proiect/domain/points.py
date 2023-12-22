import utils.helpers as h
import math
import matplotlib.pyplot as plt

class MyPoint:
    def __init__(self, coord_x, coord_y, color):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        if h.checkcolor(color):
            self.__color = color
        else:
            raise ValueError("Color is not correct!")
    
    @property
    def coord_x(self):
        return self.__coord_x

    @property
    def coord_y(self):
        return self.__coord_y

    @property
    def color(self):
        return self.__color

    def setColor(self, newColor):
        if h.checkcolor(newColor):
            self.__color = newColor
        else:
            raise ValueError("Color is not correct!")
    
    def setCoordX(self, newCoordX):
        self.__coord_x = newCoordX

    def setCoordY(self, newCoordY):
        self.__coord_y = newCoordY


    def __repr__(self):
        return f"MyPoint({self.__color}, {self.__coord_x}, {self.__coord_y})"

    def __str__(self):
        return self.__repr__()
class pointsRepository:
    def __init__(self, initialPoints=None):
        """
        Creating a repository containing points
        """
        self.__list_of_points = []
        if initialPoints is not None:
            # check if the ids are unique
            for points in initialPoints:
                if isinstance(points, MyPoint):
                    self.__list_of_students.append(points)

    def addPoints(self, coord_x, coord_y, color):
        """
        ex. 1
        Add a new point to the repository
        :param id_:
        :type id_: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        :return:
        :rtype:
        """
        self.__list_of_points.append(MyPoint(coord_x, coord_y, color))

    def getPoints(self):
        """
        ex. 2
        Get all points from the repository.
        Return a copy of the list! Otherwise, the user can change the content of the list.
        :return:
        :rtype: list
        """
        return self.__list_of_points[:]
    
    def getPointAtIndex(self, index):
        #ex. 3
        #Get a point at a given index
        return self.__list_of_points[index]
    
    def getPointsColor(self, color):
        #ex. 4
        #Get all points that are a given color
        Points = []
        for point in self.__list_of_points:
            if (point.color == color):
                Points.append(point)
        return pointsRepository(Points)

    def getPointsSquare(self, up_left_x, up_left_y, down_right_x, down_right_y):
        #ex. 5
        #Get all points that are in a given square
        Points = []
        for point in self.__list_of_points:
            if (point.coord_x >= up_left_x and point.coord_x <= down_right_x and point.coord_y >= down_right_y and point.coord_y <= up_left_y):
                Points.append(point)
        return pointsRepository(Points)

    def minDistance(self, indexpoint1, indexpoint2):
        #ex. 6
        #Get the minimum distance between two points
        point1 = self.__list_of_points[indexpoint1]
        point2 = self.__list_of_points[indexpoint2]
        distance = math.sqrt((point1.coord_x - point2.coord_x) ** 2 + (point1.coord_y - point2.coord_y) ** 2)
        return distance

    def updateAtIndex(self, index):
        #ex. 7
        #Update a point at a given index
        newCoord_x = int(input("Input new x coordinate: "))
        newCoord_y = int(input("Input new y coordinate: "))
        newColor = int(input("Input new color: "))

        indexp = len(self.__list_of_points)
        while (indexp >= 0):
            if (indexp == index):
                self.__list_of_points[index].color = newColor
                self.__list_of_points[index].coord_x = newCoord_x
                self.__list_of_points[index].coord_y = newCoord_y
                break
            else:
                indexp -= 1
    
    def delPointByIndex(self, index):
        #ex. 8
        #Delete a point by a given index
        indexp = len(self.__list_of_points)
        while (indexp >= 0):
            if (indexp == index):
                del self.__list_of_points[index]
            else:
                indexp -= 1

    def delPointsSquare(self, up_left_x, up_left_y, down_right_x, down_right_y):
        #ex. 9
        #Delete all points inside a given square
        index = len(self.__list_of_points)
        while (index >= 0):
            point = self.__list_of_points[index]
            if (point.coord_x >= up_left_x and point.coord_x <= down_right_x and point.coord_y >= down_right_y and point.coord_y <= up_left_y):
                del self.__list_of_points[index]
            index -= 1
        #idk how to do this one yet

    def PlotInChart(self):
        #ex. 10
        #Plot all points in a chart using matplotlib
        x = []
        y = []
        colors = []
        for points in self.__list_of_points:
            x.append(points.coord_x)
            y.append(points.coord_y)
            colors.append(points.color)
        fig, ax = plt.subplots()
        ax.scatter(x, y, c = colors)
        plt.show()

    def getCircle(self, center_x, center_y, radius):
        #ex. 11
        #Get a list containing all the points that are inside of a circle with given center and radius
        Points = []
        if (radius <= 0):
            raise ValueError("Radius is incorrect!")
        else:
            for point in self.__list_of_points:
                distance = math.sqrt((point.coord_x - center_x) ** 2 + (point.coord_y - center_y) ** 2)
                if (distance <= radius and distance > 0):
                    Points.append(point)
            return pointsRepository(Points)

    def getRectangle(self, up_left_x, up_left_y, length, width):
        #ex. 12
        #Get all points inside a rectangle with given up-left corner, length and width
        down_right_x = up_left_x + length
        down_right_y = up_left_y - width
        Points = []
        for point in self.__list_of_points:
            if (point.coord_x >= up_left_x and point.coord_x <= down_right_x and point.coord_y >= down_right_y and point.coord_y <= up_left_y):
                Points.append(point)
        return pointsRepository(Points)
    
    def getMaxDistance(self, indexpoint1, indexpoint2):
        #ex. 13
        #Get the maximum distance between two given points.
        #whathefuck?
        pass

    def numberOfPointsByColor(self, color):
        # ex. 14
        #Get the number of points that have color = given color
        number = 0
        for point in self.__list_of_points:
            if (point.color == color):
                number += 1
        return number

    def updateColorByCoords(self, coordx, coordy, newColor):
        #ex. 15
        #Update a point's color using given x and y coordinates
        index = len(self.__list_of_points)
        while (index >= 0):
            for point in self.__list_of_points:
                if (point.coord_x == coordx and point.coordy_y == coordy):
                    self.__list_of_points[index].color = newColor
            index -= 1
        return self.__list_of_points

    def shiftOnXAxis(self, shiftVal):
        #ex. 16
        #Shift all coordinates on the x axis by given shifting value
        index = len(self.__list_of_points)
        while (index >= 0):
            self.__list_of_points[index].coord_x += shiftVal
            index -= 1
        return self.__list_of_points
    
    def shiftOnYAxis(self, shiftedVal):
        #ex. 17
        #Shift all coordinates on the y axis by given shifting value
        index = len(self.__list_of_points)
        while (index >= 0):
            self.__list_of_points[index].coord_y += shiftedVal
            index -= 1
        return self.__list_of_points


    def delPointCoord(self, coord_x, coord_y):
        #ex. 18
        #Delete a point by given coordinates
        index = len(self.__list_of_points) - 1
        while (index >= 0):
            point = self.__list_of_points[index]
            if (point.coord_x == coord_x and point.coord_y == coord_y):
                del self.__list_of_points[index]
            index -= 1
        return self.__list_of_points

    def delPointsCircle(self, center_x, center_y, radius):
        #ex. 19
        #Delete all points inside a given circle
        Points = []
        if (radius <= 0):
            raise ValueError("Radius is incorrect!")
        else:
            index = len(self.__list_of_points)
            while (index >= 0):
                point = self.__list_of_points[index]
                distance = math.sqrt((point.coord_x - center_x) ** 2 + (point.coord_y - center_y) ** 2)
                if (distance <= radius and distance > 0):
                    del self.__list_of_points[index]
            return self.__list_of_points
    
    def delPointsGivenDistance(self, coordxpoint, coordypoint, distance):
        #ex. 20
        #Delete all points that are within a certain given distance from a given point
        if (distance <= 0):
            raise ValueError("Distance given incorrecntly!")
        else:
            index = len(self.__list_of_points)
            while (index >= 0):
                point = self.__list_of_points[index]
                newDist = math.sqrt((point.coord_x - coordxpoint) ** 2 + (point.coord_y - coordypoint) ** 2)
                if (newDist <= distance):
                    del self.__list_of_points[index]
                index -= 1
            return self.__list_of_points
        

pr = pointsRepository()
pr.addPoints(2, 5, "red")
pr.addPoints(2, 6, 'blue')
pr.addPoints(3, 9, 'green')
pr.addPoints(-5, 6, 'yellow')
# x = int(input("Coordinate x: "))
# y = int(input("Coordinate y: "))
# color = input("Color: ")
# point = MyPoint(x, y, color)
# print(point.color)
# MyPoint.getCircle(-2, 3, 5)
# print(pr.getPoints())
# pr.PlotInChart()

class Book:
    def __init__(self, numOfPages, title):
        self.__numOfPages = self.__checkNumOfPages(numOfPages)
        self.__title = title

    @staticmethod
    def __checkNumOfPages(numOfPages):
        if numOfPages > 0:
            return numOfPages
        else:
            raise ValueError("Number of pages is not positive")

    def getNumOfPages(self):
        return self.__numOfPages

    def getTitle(self):
        return self.__title

    def setNumOfPages(self, numOfPages):
        self.__numOfPages = self.__checkNumOfPages(numOfPages)

    def setTitle(self, title):
        self.__title = title

    def __repr__(self):
        return f"Book({self.__numOfPages}, {self.__title})"

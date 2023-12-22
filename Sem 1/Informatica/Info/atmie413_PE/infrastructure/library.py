from domain.book import Book
from utils.filterPersonal import searchBy

class BookRepository:
    def __init__(self, BookList = None):
        self.__BookList = []
        if BookList is not None:
            for book in BookList:
                if isinstance(book, Book) and self.isUnique(book.getTitle()):
                    self.__BookList.append(book)

    def isUnique(self, title):
        for book in self.__BookList:
            if book.getTitle() == title:
                return False
        return True

    def updateBook(self, index, numOfPages, title):
        if index > 0 and index < len(self.__BookList):
            searchedBook = self.__BookList[index]
            if numOfPages > 0 and self.isUnique(title):
                searchedBook.setNumOfPages(numOfPages)
                searchedBook.setTitle(title)
            else:
                raise ValueError("Something is wrong")
        else:
            raise ValueError("Index not correct")

    def getBooksNumOfPagesMaximum(self):
        max = -1
        for book in self.__BookList:
            if book.getNumOfPages() > max:
                max = book.getNumOfPages()

        return BookRepository(filter(lambda book: book.getNumOfPages() == max, self.__BookList))

    def getAllBooks1(self, value):
        return BookRepository(filter(lambda book: len(book.getTitle()) == value, self.__BookList))

    def getAllBooks2(self, value):
        return searchBy(self.__BookList, condition=lambda x: len(x.getTitle()) == value)

    def __repr__(self):
        return str(self.__BookList)

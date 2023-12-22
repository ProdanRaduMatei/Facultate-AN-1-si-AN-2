import domain.book as book


class Repository:
    def __init__(self, BookList=None):
        self.__BookList = []
        if BookList is not None:
            for Book in BookList:
                if isinstance(Book, book.Books) and self.__isunique(Book.name):
                    self.__BookList.append(Book)
                else:
                    raise ValueError("Not a Book!")

    def __isunique(self, name):
        for Book in self.__BookList:
            if Book.name == name:
                return False
        return True
    
    def __isIndexCorrect(self, index):
        """
        Check if the index is correct in the list of books
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__BookList) or 0 == index == len(self.__BookList)

    def addBook(self, name, pages):
        """
        Add a new Book.
        :param name: name
        :param pages: pages
        :return: Book
        """
        if not self.__isunique(name):
            self.__BookList.append(book.Books(name, pages))
        else:
            raise ValueError("Name is not a name.")
        
    def deleteAtIndex(self, index):
        """
        Delete a Book at a given index
        :param index:
        :type index: int
        """
        if self.__isIndexCorrect(index):
            del self.__BookList[index]
        else:
            raise IndexError("Index is not correct!")

    def getBooksWithAvgPages(self):
        avgpages = 0
        for Books in enumerate(self.__BookList):
            avgpages = avgpages + Books.pages
        avgpages = avgpages / len(self.__BookList)
        return Repository(filter(lambda Book: Book.pages == avgpages, self.__BookList))

    def UpdateBookByName(self, name, pages, category):
        if not self.__isunique(name):
            for index, Book in enumerate(self.__BookList):
                if Book.name == name:
                    self.__BookList[index].pages = pages
                    self.__BookList[index].category = category
        else:
            raise ValueError("Not a name.")

    def FilterBook(self, title):
        return Repository(filter(lambda Book: Book.name == title, self.__BookList))

    def SortBookpages(self):
        return Repository(sorted(self.__BookList, key = lambda Book: Book.pages))

    def __repr__(self):
        return str(self.__BookList)
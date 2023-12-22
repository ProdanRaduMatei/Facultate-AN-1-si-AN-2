class Book:
    def __init__(self, name, pages):
        self.__name = name
        if pages <= 0:
            self.__pages = pages
        else:
            raise ValueError("pages is not correct!")
        

    @property
    def name(self):
        return self.__name
    @property
    def pages(self):
        return self.__pages

    @name.setter
    def name(self, other_name):
        self.__name = other_name
    @pages.setter
    def pages(self, other_pages):
        self.__pages = other_pages

    def __repr__(self):
        return f"Book({self.__name}, {self.__pages})"

    def __sbr__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.__name == other.__pages or self.__pages == other.__pages
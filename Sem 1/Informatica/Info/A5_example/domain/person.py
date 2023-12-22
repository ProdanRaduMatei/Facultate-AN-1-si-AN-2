class Person:   # Passenger, Patient
    def __init__(self, id_, firstname, lastname):
        self.__id = id_
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def ID(self):
        # TODO: implement
        pass

    @property
    def firstname(self):
        # TODO: implement
        pass

    @property
    def lastname(self):
        # TODO: implement
        pass

    @ID.setter
    def ID(self, newId):
        # TODO: implement
        pass

    @firstname.setter
    def firstname(self, newFirstname):
        # TODO: implement
        pass

    @lastname.setter
    def lastname(self, newLastname):
        # TODO: implement
        pass

from infrastructure.repositories import PersonRepositoryRepository


class Controller:
    def __init__(self):
        self.__repo = PersonRepositoryRepository()

    def c_example(self):
        # TODO: call example function of the repository.
        # if the function returns a value use return in this function too
        return self.__repo.example()

    # TODO: create same functions for the rest of the functions from PersonRepositoryRepository

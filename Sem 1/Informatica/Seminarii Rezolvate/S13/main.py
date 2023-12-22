from domain.backpack import Backpack
from domain.object import Object
from infrastructure.store import Store


class Solution:
    def __init__(self, store, maxWeight):
        self.__store = store
        self.__backpack = Backpack(maxWeight)

    @property
    def store(self):
        """
        Get the store from the solution
        :return:
        :rtype:
        """
        return self.__store

    @property
    def backpack(self):
        """
        Get the backpack (the final solution of the problem)
        :return:
        :rtype:
        """
        return self.__backpack

    def run(self):
        """
        Solve the backpack problem
        :return:
        :rtype:
        """
        self.__store.sort()
        for i in range(self.__store.lengthListOfObj()):
            try:
                self.__backpack.put(self.__store[i])
            except ValueError:
                continue
            print("new item added")


if __name__ == "__main__":
    s = Store([Object(100, 2), Object(1, 1), Object(200, 10),
               Object(50, 1.5), Object(50, 2)])
    greedySolution = Solution(s, 4.5)
    greedySolution.run()
    print(greedySolution.store)
    print(greedySolution.backpack)

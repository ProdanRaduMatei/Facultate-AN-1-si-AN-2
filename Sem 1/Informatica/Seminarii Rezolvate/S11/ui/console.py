class Console:
    def __init__(self, shapeController):
        self.__controller = shapeController

    @staticmethod
    def menuOptions():
        print(f"{'e':>3} - Exit")
        print(f"{'h':>3} - Print options")
        print(f"{'1':>3} - Print shapes")
        print(f"{'2':>3} - Print shapes with more than k sides")
        print(f"{'3':>3} - Print shapes with perimeter higher than a given "
              f"value and it's name's length is another given value")
        print(f"{'4':>3} - Sort shapes by perimeter")
        print(f"{'5':>3} - Sort shapes with name starting with a given sequence by perimeter")

    def start(self):
        Console.menuOptions()
        print(self.__controller)
        choice = input(">>> ")
        while choice != "e":
            if choice == "h":
                Console.menuOptions()
            elif choice == "1":
                print(self.__controller)
            elif choice == "2":
                try:
                    k = int(input("k = "))
                    print("CUSTOM")
                    print(self.__controller.more_than_k_sides(k))
                    print("IN-BUILT")
                    print(self.__controller.more_than_k_sides_in_built(k))
                except ValueError:
                    print(f"k should be a valid integer")
            elif choice == "3":
                try:
                    min_perimeter = int(input("Minimum perimeter = "))
                    name_length = int(input("Length of the name = "))
                    print("CUSTOM")
                    print(self.__controller.higher_perimeter(min_perimeter, name_length))
                    print("IN-BUILT")
                    print(self.__controller.higher_perimeter_in_built(min_perimeter, name_length))
                except ValueError:
                    print(f"Minimum perimeter value and name length should be a valid integers")
            elif choice == "4":
                desc = input("Do you want to order descending? (y/n) ")
                print("CUSTOM")
                print(self.__controller.sort_by_perimeter(desc in "yY"))
                print("IN-BUILT")
                print(self.__controller.sort_by_perimeter_in_built(desc in "yY"))
            elif choice == "5":
                desc = input("Do you want to order descending? (y/n) ")
                name_prefix = input("Prefix of the shape name = ")
                print("CUSTOM")
                print(self.__controller.sort_name_starting_by_perimeter(name_prefix, desc in "yY"))
                print("IN-BUILT")
                print(self.__controller.sort_name_starting_by_perimeter_in_built(name_prefix, desc in "yY"))
            elif choice == "":
                pass
            else:
                print(f"{choice} option not defined")
            choice = input(">>> ")

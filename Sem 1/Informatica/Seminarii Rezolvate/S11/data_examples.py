from utils.sort import *
from utils.search import *
from utils import criterions


def search_examples():
    """
    Search function examples.
    """
    a = [1, 9, 5, 8, 4, 2, 3, 0]
    sorted_a = sorted(a)
    print("seminar 9. ii. 1. SEQUENTIAL SEARCH")
    print(f"UNORDERED LIST\t{a = }")
    print(f"\t{sequentialSearchUnordered(a, 6) = }")
    print(f"\t{sequentialSearchUnordered(a, 1) = }")
    print(f"\t{sequentialSearchUnordered(a, 8) = }")
    print(f"ORDERED LIST\t{sorted_a = }")
    print(f"\t{sequentialSearchOrdered(sorted_a, 6) = }")
    print(f"\t{sequentialSearchOrdered(sorted_a, 1) = }")
    print(f"\t{sequentialSearchOrdered(sorted_a, 8) = }")


def filter_examples():
    """
    Filter function examples.
    """
    a = [370, 2, 1, 407, 153, 16, 25, 17, 0, 371, 37]
    print("\nFILTER LIST VALUES")
    print(f"{a = }")
    print("seminar 10. i. 1.")
    print(f"\t{myFilter(a, criterions.isArmstrong) = }")
    print(f"\t{inBuiltFilter(a, criterions.isArmstrong) = }")
    print("seminar 10. i. 2.")
    print(f"\t{myFilter(a, criterions.criterion_i_2) = }")
    print(f"\t{inBuiltFilter(a, criterions.criterion_i_2) = }")
    print("seminar 10. i. 3.")
    print(f"\t{myFilter(a, criterions.criterion_i_3) = }")
    print(f"\t{inBuiltFilter(a, criterions.criterion_i_3) = }")


def sort_examples():
    """
    Sort function examples.
    """
    a = [370, 2, 1, 407, 153, 16, 25, 17, 0, 371, 37]
    print(f"{a = }")
    print("\nSORT LIST VALUES")
    print("seminar 10. ii. 1. BUBBLE SORT")
    print(f"\tfunction call:\t bubbleSort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{bubbleSort(a.copy())}")
    print("seminar 10. ii. 2. SELECTION SORT")
    print("\tMINIMUM SELECTION")
    print(f"\t\tfunction call:\t minimumSelectionSort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{minimumSelectionSort(a.copy())}")
    print("\tMAXIMUM SELECTION")
    print(f"\t\tfunction call:\t maximumSelectionSort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{maximumSelectionSort(a.copy())}")


def run_all():
    """
    Print all data examples
    """
    search_examples()
    filter_examples()
    sort_examples()

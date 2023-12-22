from utils.sort import *
from utils.search import *
from utils.back_track import getSolutions
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
    print(f"BINARY SEARCH\t{sorted_a = }")
    print(f"\t{binarySearch(sorted_a, 6) = }")
    print(f"\t{binarySearch(sorted_a, 1) = }")
    print(f"\t{binarySearch(sorted_a, 8) = }")


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
    print(f"\tfunction call:\t bubble_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{bubbleSort(a.copy())}")
    print("seminar 10. ii. 2. SELECTION SORT")
    print("\tMINIMUM SELECTION")
    print(f"\t\tfunction call:\t minimum_selection_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{minimumSelectionSort(a.copy())}")
    print("\tMAXIMUM SELECTION")
    print(f"\t\tfunction call:\t maximum_selection_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{maximumSelectionSort(a.copy())}")
    print("seminar 10. ii. 3. INSERTION SORT")
    print(f"\tfunction call:\t insertion_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{insertionSort(a.copy())}")
    print("seminar 10. ii. 4. QUICK SORT")
    print(f"\tfunction call:\t quick_sort(a.copy())")
    print(f"\tinput:\t{a}")
    print(f"\toutput:\t{recursiveQuickSort(a.copy())}")
    print("seminar 10. GENERAL SORT")
    print("\tASCENDING")
    print(f"\t\tfunction call:\t my_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{mySort(a.copy())}")
    print("\tDESCENDING")
    print(f"\t\tfunction call:\t my_sort(a.copy(), lambda x, y: x > y)")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{mySort(a.copy(), lambda x, y: x > y)}")
    print("seminar 10. IN BUILT SORT")
    print("\tASCENDING")
    print(f"\t\tfunction call:\t in_built_sort(a.copy())")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{sorted(a.copy())}")
    print("\tDESCENDING")
    print(f"\t\tfunction call:\t in_built_sort(a.copy(), lambda x, y: x > y)")
    print(f"\t\tinput:\t{a}")
    print(f"\t\toutput:\t{sorted(a.copy(), reverse=True)}")


def backtrack_examples():
    print("\nBACKTRACK ALGORITHM")
    print("PERMUTATIONS OF 3")

    possible_values = [4, 5, 6]

    def unique_values(currentSolution):
        if len(currentSolution) == len(set(currentSolution)):
            return True
        else:
            return False

    # isConsistentFn=lambda currentSolution: len(currentSolution) == len(set(currentSolution))

    print("\tRECURSIVE")
    print("\t",
          getSolutions(possible_values, doesElementExistFn=lambda element: element < 3, isConsistentFn=unique_values,
                       isSolutionFn=lambda currentSolution: len(currentSolution) == 3))
    print("\tITERATIVE")
    print("\t", getSolutions(possible_values, doesElementExistFn=lambda element: element < 3,
                             isConsistentFn=unique_values, isSolutionFn=lambda currentSolution: len(currentSolution) == 3,
                             iterative=True))

    print("GROUP OF 2 FROM NUMBERS 1 TO 3")
    print("\tRECURSIVE")
    print("\t", getSolutions(possible_values, doesElementExistFn=lambda element: element < 3,
                             isConsistentFn=unique_values,
                             isSolutionFn=lambda currentSolution: len(currentSolution) == 2))
    print("\tITERATIVE")
    print("\t", getSolutions(possible_values, doesElementExistFn=lambda element: element < 3,
                             isConsistentFn=unique_values, isSolutionFn=lambda currentSolution: len(currentSolution) == 2,
                             iterative=True))


def run_all():
    """
    Print all data examples
    """
    search_examples()
    filter_examples()
    sort_examples()
    backtrack_examples()

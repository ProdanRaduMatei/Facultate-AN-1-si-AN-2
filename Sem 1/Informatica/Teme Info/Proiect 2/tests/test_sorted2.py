from utilities.sorted2 import SortValuesGreater

def TestSortValuesGreater():
    score_list = [5, 4, 3, 2, 1]
    sorted_list = SortValuesGreater(score_list, 0)
    assert sorted_list == [1, 2, 3, 4, 5]

from utilities.sorted1 import SortAllValues

def TestSortAllValues():
    score_list = [7, 6, 5]
    index_list = SortAllValues(score_list)
    assert index_list == [2, 1, 0]

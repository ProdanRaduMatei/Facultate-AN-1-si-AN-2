from utilities.print_array import PrintArray

def TestPrintArray():
    score_list = [5]
    PrintArray(score_list)
    assert score_list == [5]
    
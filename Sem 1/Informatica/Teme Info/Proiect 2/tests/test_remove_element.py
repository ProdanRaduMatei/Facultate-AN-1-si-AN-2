from utilities.remove_element import RemoveElement

def TestRemoveElement():
    score_list = [5, 6]
    new_score_list = RemoveElement(score_list, 1)
    assert new_score_list == [5]
from utilities.remove_interval import RemoveInterval

def TestRemoveInterval():
    score_list = [5, 6, 7]
    new_score_list = RemoveInterval(score_list, 1, 2)
    assert new_score_list == [5]
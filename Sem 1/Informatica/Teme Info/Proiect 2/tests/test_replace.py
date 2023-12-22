from utilities.replace import Replace

def TestReplace():
    score_list = [5]
    new_score_list = Replace(score_list, 0, 6)
    assert new_score_list == [6]
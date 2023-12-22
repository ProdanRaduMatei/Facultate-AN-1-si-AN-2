from utilities.less import Less

def TestLess():
    score_list = [5]
    new_score_list = Less(score_list, 5)
    assert new_score_list == []

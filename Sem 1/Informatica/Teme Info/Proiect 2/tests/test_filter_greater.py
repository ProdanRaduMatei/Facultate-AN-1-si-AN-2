from utilities.filter_greater import FilterGreater

def TestFilterGreater():
    score_list = [5]
    new_score_list = FilterGreater(score_list, 5)
    assert new_score_list == []
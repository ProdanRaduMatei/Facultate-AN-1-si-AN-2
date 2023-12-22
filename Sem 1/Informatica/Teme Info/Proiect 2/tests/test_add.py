from utilities.add import Add

def TestAdd():
    score_list = []
    Add(score_list, 5)
    assert score_list == [5]

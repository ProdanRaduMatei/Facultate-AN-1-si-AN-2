from utilities.insert import Insert

def TestInsert():
    score_list = []
    new_score_list = Insert(score_list, 0, 5)
    assert new_score_list == [5]
    
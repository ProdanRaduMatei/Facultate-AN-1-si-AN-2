def Insert(score_list, index, value): # this function inserts a value at an index
    score_list.insert(index, value) # inserts the value at the index
    return score_list # returns the list

def TestInsert():
    score_list = []
    Insert(score_list, 0, 5)
    assert score_list == [5]
    
    try:
        Insert(score_list, 0, 2)
        assert True
    except ValueError:
        assert False
    
    try:
        Insert(score_list, 1, 11)
        assert False
    except ValueError:
        assert True
    
    try:
        Insert(score_list, 0, 'a')
        assert False
    except ValueError:
        assert True

#TestInsert()
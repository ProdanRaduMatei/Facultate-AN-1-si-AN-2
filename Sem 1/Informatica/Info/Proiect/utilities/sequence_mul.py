def SequenceMul(score_list, value, index1, index2): # this function gets the scores multiples of a value between two indexes
    new_score_list = []
    for i in range(index1, index2 + 1): # goes through the list between the indexes
        if score_list[i] % value == 0: # checks if the score is multiple of the value
            new_score_list.append(score_list[i]) # puts the score in a new list
    return new_score_list # returns the list

def TestSequenceMul():
    score_list = [5]
    SequenceMul(score_list, 1, 0, 0)
    assert score_list == [5]
    
    try:
        SequenceMul(score_list, 5, 0, 0)
        assert True
    except ValueError:
        assert False
    
    try:
        SequenceMul(score_list, 2, 11, 100)
        assert False
    except ValueError:
        assert True
    
    try:
        SequenceMul(score_list, 'a', 'b', 'c')
        assert False
    except ValueError:
        assert True

#TestSequenceMul()
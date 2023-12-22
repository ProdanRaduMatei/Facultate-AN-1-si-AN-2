from turtle import st

def RemoveInterval(score_list, start, end): # this function deletes the scores between two indexes
    del score_list[start : end + 1] # removes the values between the indexes
    return score_list # returns the list

def TestRemoveInterval():
    score_list = [5, 6, 7]
    RemoveInterval(score_list, 0, 1)
    assert score_list == [7]
    
    try:
        RemoveInterval(score_list, 0, 0)
        assert True
    except ValueError:
        assert False
    
    try:
        RemoveInterval(score_list, 11, 100)
        assert False
    except ValueError:
        assert True
    
    try:
        RemoveInterval(score_list, 'a', 'b')
        assert False
    except ValueError:
        assert True

#TestRemoveInterval()
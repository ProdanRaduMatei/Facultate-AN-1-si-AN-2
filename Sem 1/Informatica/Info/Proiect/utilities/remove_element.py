def RemoveElement(score_list, index): #this function removes a score at a certain index
    del score_list[index] # removes the score at the index
    return score_list # return the list

def TestRemoveElement():
    score_list = [5, 6]
    RemoveElement(score_list, 0)
    assert score_list == [6]
    
    try:
        RemoveElement(score_list, 0)
        assert True
    except ValueError:
        assert False
    
    try:
        RemoveElement(score_list, 11)
        assert False
    except ValueError:
        assert True
    
    try:
        RemoveElement(score_list, 'a')
        assert False
    except ValueError:
        assert True

#TestRemoveElement()
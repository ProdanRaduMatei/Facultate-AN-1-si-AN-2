def SequenceMin(score_list, index1, index2): # this function gets the minimum score between two indexes
    minimum = 11
    for i in range(index1, index2 + 1): # goes through the list between the indexes
        if score_list[i] < minimum: # checks if the score is smaller than the minimum
            minimum = score_list[i] # updates the minimum
    return minimum # returns the minimum

def TestSequenceMin():
    score_list = [5]
    SequenceMin(score_list, 0, 0)
    assert score_list == [5]
    
    try:
        SequenceMin(score_list, 0, 0)
        assert True
    except ValueError:
        assert False
    
    try:
        SequenceMin(score_list, 11, 100)
        assert False
    except ValueError:
        assert True
    
    try:
        SequenceMin(score_list, 'a', 'b')
        assert False
    except ValueError:
        assert True

#TestSequenceMin()
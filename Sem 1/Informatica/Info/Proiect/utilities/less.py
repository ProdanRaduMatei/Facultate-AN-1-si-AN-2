def Less(score_list, value): # this function gets the scores smaller than a value
    new_list = []
    for i in range(0, len(score_list)): # goes through the list
        if i < value: # compares the score to the value
            new_list.append(i) # puts the score into a new list
    return new_list # returns the list

def TestLess():
    score_list = [5]
    Less(score_list, 6)
    assert score_list == [5]
    
    try:
        Less(score_list, 9)
        assert True
    except ValueError:
        assert False
    
    try:
        Less(score_list, 1)
        assert False
    except ValueError:
        assert True
    
    try:
        Less(score_list, 'a')
        assert False
    except ValueError:
        assert True

#TestLess()
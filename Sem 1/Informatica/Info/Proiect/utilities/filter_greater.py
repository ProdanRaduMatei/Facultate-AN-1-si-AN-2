def FilterGreater(score_list, value): # this function gets the scores greater than a value
    new_score_list = []
    for i in score_list: # goes through the list
        if i > value: # compares the score to the value
            new_score_list.append(i) # puts the score in a new list
    return new_score_list # returns the list


def TestFilterGreater():
    score_list = [5]
    FilterGreater(score_list, 5)
    assert score_list == [5]
    
    try:
        FilterGreater(score_list, 6)
        assert True
    except ValueError:
        assert False
    
    try:
        FilterGreater(score_list, 11)
        assert False
    except ValueError:
        assert True
    
    try:
        FilterGreater(score_list, 'a')
        assert False
    except ValueError:
        assert True

#TestFilterGreater()
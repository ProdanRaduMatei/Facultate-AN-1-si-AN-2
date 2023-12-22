def Replace(score_list, index, new_value): # this function replaces the score at an index with a value
    score_list[index] = new_value # replaces the score at index with a value
    return score_list # returns the list

def TestReplace():
    score_list = [5]
    Replace(score_list, 0, 1)
    assert score_list == [1]
    
    try:
        Replace(score_list, 0, 0)
        assert True
    except ValueError:
        assert False
    
    try:
        Replace(score_list, 11, 100)
        assert False
    except ValueError:
        assert True
    
    try:
        Replace(score_list, 'a', 'b')
        assert False
    except ValueError:
        assert True

#TestReplace()
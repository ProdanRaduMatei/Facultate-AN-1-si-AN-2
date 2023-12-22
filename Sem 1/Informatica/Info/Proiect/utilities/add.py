def Add(score_list, value): # this function adds a value to the end of the list
    score_list.append(value) # adds the value to the list
    return score_list # returns the list

def TestAdd():
    score_list = []
    Add(score_list, 5)
    assert score_list == [5]
    
    try:
        Add(score_list, 6)
        assert True
    except ValueError:
        assert False
    
    try:
        Add(score_list, 11)
        assert False
    except ValueError:
        assert True
    
    try:
        Add(score_list, 'a')
        assert False
    except ValueError:
        assert True

#TestAdd()

#print(Add([], 0))
#print(Add([0], 1))
#print(Add([], 0))
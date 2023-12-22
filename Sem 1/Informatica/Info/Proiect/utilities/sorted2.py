

def SortValuesGreater(score_list, value):
    #Create a sorted list with participants with score higher than value given
    if (utils.checkValue(value) == True):
        sortl = []
        indexlist = []
        sortl = score_list[:]
        sortl.sort()
        sortl = list(set(sortl))
        for i in range(len(sortl)):
            for j in range(len(score_list)):
                if (score_list[j] == sortl[i] and score_list[j] > value):
                    indexlist.append(j)
        return indexlist

def TestSortValuesGreater():
    score_list = [5]
    SortValuesGreater(score_list, 1)
    assert score_list == [5]
    
    try:
        SortValuesGreater(score_list, 2)
        assert True
    except ValueError:
        assert False
    
    try:
        SortValuesGreater(score_list, 11)
        assert False
    except ValueError:
        assert True
    
    try:
        SortValuesGreater(score_list, 'a')
        assert False
    except ValueError:
        assert True

#TestSortValuesGreater()
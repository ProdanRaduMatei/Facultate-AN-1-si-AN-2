from utilities.filter_mul import FilterMul

def TestFilterMul():
    #only good values
    score_list = [5, 6, 7]
    new_score_list = FilterMul(score_list, 5)
    assert new_score_list == [5]

def SortValuesGreater(score_list, value): # this function gets the scores greater than a value sorted
    for i in range(0, len(score_list)): # goes through the list
        for j in range(i + 1, len(score_list)): # goes through the list
            if score_list[i] > score_list[j]: # checks if the numbers are in order
                aux = score_list[i]
                score_list[i] = score_list[j]
                score_list[j] = aux
    new_score_list = []
    for i in score_list: # goes through the list
        if i > value: # checks if the score is greater than the value
            new_score_list.append(i) # adds the value in new list
    return new_score_list # returns the list

#TestSortValuesGreater()
def Less(score_list, value): # this function gets the scores smaller than a value
    new_list = []
    for i in score_list: # goes through the list
        if i < value: # compares the score to the value
            new_list.append(i) # puts the score into a new list
    return new_list # returns the list

#TestLess()
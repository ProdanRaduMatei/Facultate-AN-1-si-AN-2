def FilterGreater(score_list, value): # this function gets the scores greater than a value
    new_score_list = []
    for i in score_list: # goes through the list
        if i > value: # compares the score to the value
            new_score_list.append(i) # puts the score in a new list
    return new_score_list # returns the list

#TestFilterGreater()
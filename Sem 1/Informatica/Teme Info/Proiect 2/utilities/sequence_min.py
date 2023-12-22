def SequenceMin(score_list, index1, index2): # this function gets the minimum score between two indexes
    minimum = 11
    for i in range(index1, index2 + 1): # goes through the list between the indexes
        if score_list[i] < minimum: # checks if the score is smaller than the minimum
            minimum = score_list[i] # updates the minimum
    return minimum # returns the minimum

#TestSequenceMin()
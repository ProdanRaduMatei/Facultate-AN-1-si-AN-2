def SequenceAvg(score_list, index1, index2): # this function gets the average score between two indexes
    s = 0 # the sum is initialised with 0
    for i in range(index1, index2 + 1): # goes through the list between the indexes
        s += score_list[i] # adds to the sum
    avg = float(s / (index2 - index1 + 1)) # gets the average score
    return avg # returns the average

#TestSequenceAvg()
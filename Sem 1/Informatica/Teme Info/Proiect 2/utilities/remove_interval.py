from turtle import st

def RemoveInterval(score_list, start, end): # this function deletes the scores between two indexes
    del score_list[start : end + 1] # removes the values between the indexes
    return score_list # returns the list

#TestRemoveInterval()
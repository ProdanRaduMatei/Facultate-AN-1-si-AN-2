def Undo(old_score_list, current_score_list): # this function undos the last operation that modified the list
    current_score_list = old_score_list.copy() # copies the old list into the current list
    return current_score_list # returns the list
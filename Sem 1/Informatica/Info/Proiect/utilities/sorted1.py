from operator import index

def SortAllValues(score_list):
    #Just sort the list by their scores
    sortl = []
    indexlist = []
    sortl = score_list[:]
    sortl.sort()
    sortl = list(set(sortl))
    for i in range(len(sortl)):
        for j in range(len(score_list)):
            if (score_list[j] == sortl[i]):
                indexlist.append(j)
    return indexlist
from operator import index


def SortAllValues(score_list): # this function sorts the list
    indexList = []
    for i in range(0, len(score_list)):
        indexList.append(i)
    for i in range(0, len(score_list)):
        for j in range(i + 1, len(score_list)):
            if score_list[i] > score_list[j]:
                aux = score_list[i]
                score_list[i] = score_list[j]
                score_list[j] = aux
                aux = indexList[i]
                indexList[i] = indexList[j]
                indexList[j] = aux
    return indexList # returns the list
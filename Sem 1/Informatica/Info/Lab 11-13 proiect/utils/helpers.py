def checkCNP(cnp):
    if cnp/100000 >= 1 and cnp/100000 <= 6:
        return 1
    else:
        return 0

def CheckList(list):
    if list == "patient1":
        return True
    else:
        return False
def checkdisease(disease):
    if disease == "flu" or "" or "cancer" or "leucemia":
        return True
    else:
        return False
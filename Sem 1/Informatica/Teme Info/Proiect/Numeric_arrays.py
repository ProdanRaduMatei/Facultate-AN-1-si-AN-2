from os import sched_param
import re


def Message(): #this function prints a message for UI and is like a menu
    print("Insert the number of the action you want to be done:")
    print("Actions:")
    print("0. End the programme.")
    print("1. Add the result of a new participant to the array.")
    print("2. Modify the scores in the array.")
    print("3. Get the participants with scores having some properties.")
    print("4. Obtain different characteristics of participants.")
    print("5. Filter values.")
    print("6. Undo")
    print("7. Print the participants array.")

def ReadCase(): #this function is part of the menu and reads the case from the user
    case = (int(input("Action = ")))
    return case

def ReadNewParticipant(): #this function reads the participant that is going to be inserted
    participant = int(input("New participant = "))
    return participant

def AddNewParticipant(score_list, value): #this function adds the participant to the score list at the end
    score_list.append(value)
    return score_list #it returns the list
    
def InsertNewParticipant(score_list, index, value): #this function inserts a participant at a certain index in the list
    score_list.append(0)
    L = len(score_list)
    for i in range(L - 1, index + 1): #moves the elements in the list to make space for the new participant 
        score_list[i + 1] = score_list[i]
    score_list[index] = value
    return score_list


def RemoveElement(score_list, index): # this function removes an element from the list
    L = len(score_list)
    for i in range(index, L + 1):
        score_list[i] = score_list[i + 1] # moves the elements in the list to delete the specified element
    del score_list[-1] # deletes the last element
    return score_list

def RemoveElementBetween(score_list, begining, ending): # this function removes the elements between two index
    L = len(score_list)
    for i in range(ending, L + 1):
        score_list[i - ending - begining - 1] = score_list[i] # moves the elements in the list to delete the specified elements
    return score_list

def ChangeElement(score_list, index, value): # this function changes the value of an element
    score_list[index] = value
    return score_list

def PrintArray(score_list): # this function prints the array
    print(score_list)

if __name__ == '__main__':
    score_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    Message()
    case = (int(ReadCase()))
    nrParticipants = int(0)
    score_list = []
    while case != 0:
        if case == 1:
            value = (int(ReadNewParticipant()))
            print("If you want to add the participant at the end of the list insert 1, else insert 2 and the position where you want to be put in the list.")
            action = (int(input("Action = ")))
            if action == 1:
                score_list = AddNewParticipant(score_list, value)
            else:
                index = (int(input("Index = ")))
                score_list = InsertNewParticipant(score_list, index, value)
        elif case == 2:
            print("If you want to remove an element form the list insert 1 and the index, else insert 2 and the index of the two boundaries if you want to remove more elements, or 3 and the value if you want to replace something. ")
            action = (int(input("Action = ")))
            if action == 1:
                index = (int(input("Index = ")))
                score_list = RemoveElement(score_list, index)
            elif action == 2:
                index1 = (int(input("First index = ")))
                index2 = (int(input("Second index = ")))
                score_list = RemoveElementBetween(score_list, index1, index2)
            else:
                index = (int(input("Index = ")))
                newValue = (int(input("Value = ")))
                score_list = ChangeElement(score_list, index, newValue)
        elif case == 7:
            PrintArray(score_list)
        ReadCase()
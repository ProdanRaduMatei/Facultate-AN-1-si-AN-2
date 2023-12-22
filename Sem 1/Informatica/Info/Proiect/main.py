from UI.menu_message import Message
from UI.read_case import ReadCase
from UI.read_index import ReadIndex
from UI.read_value import ReadValue
from utilities.add import Add
from utilities.filter_greater import FilterGreater
from utilities.filter_mul import FilterMul
from utilities.insert import Insert
from utilities.less import Less
from utilities.print_array import PrintArray
from utilities.remove_element import RemoveElement
from utilities.remove_interval import RemoveInterval
from utilities.replace import Replace
from utilities.sequence_avg import SequenceAvg
from utilities.sequence_min import SequenceMin
from utilities.sequence_mul import SequenceMul
from utilities.sorted1 import SortAllValues
from utilities.sorted2 import SortValuesGreater
from utilities.undo import Undo

print(Message()) # prints the menu
case = ReadCase() # reads the case
while case < 0 or case > 7:
    print("Wrong value! The case value needs to be between 0 and 7. Insert again!")
    case = ReadCase() # reads the case
score_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # score list is initiated
prev_score_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

while case != 0:
    if case == 1:
        prev_score_list = score_list.copy()
        print("You chose to add a score in the list. If you want to add it at the end of the list insert 1 and the value, else insert 2, the index and the value.")
        sub_case = ReadCase() # reads the case
        if sub_case == 1:
            value = ReadValue() # reads the value
            score_list = Add(score_list, value) # adds new value
            
        elif sub_case == 2:
            index = ReadIndex() # reads the index
            while index < 0 or index >= len(score_list):
                print("Wrong index!")
                index = ReadIndex()
            value = ReadValue() # reads the value
            score_list = Insert(score_list, index, value) # inserts new value
            
    elif case == 2:
        prev_score_list = score_list.copy()
        print("You chose to modify a score in the list. If you want to remove an element insert 1 and the index, else if  insert 2, the index and the value.")
        sub_case = ReadCase() # reads the case
        if sub_case == 1:
            index = ReadIndex() # reads the index
            while index < 0 or index >= len(score_list):
                print("Wrong index!")
                index = ReadIndex() # reads the index
            score_list = RemoveElement(score_list, index) # removes a value
            
        elif sub_case == 2:
            index1 = ReadIndex() # reads the index
            while index1 < 0 or index1 >= len(score_list):
                print("Wrong index!")
                index1 = ReadIndex() # reads the index
            index2 = ReadIndex() # reads the index
            while index2 < 0 and index2 >= len(score_list):
                print("Wrong index!")
                index2 = ReadIndex() # reads the index
            if index1 > index2:
                aux = index1
                index1 = index2
                index2 = aux
            score_list = RemoveInterval(score_list, index1, index2) # removes elements between indexes
        
        elif sub_case == 3:
            index = ReadIndex() # reads the index
            while index < 0 or index >= len(score_list):
                print("Wrong index!")
                index = ReadIndex() # reads the index
            value = ReadValue() # reads the value
            while value < 0 or value > 10:
                print("Wrong value!")
                value = ReadValue() # reads the value
            score_list = Replace(score_list, index, value) # replaces the value
            
    elif case == 3:
        prev_score_list = score_list.copy()
        print("You chose to get the participants with scores having some properties. Insert 1 and a value if you want to get the participants with score less than that value, else if you insert 2 you will get all the participants sorted by their score, else if you insert 3 and a value you will get the participants with scores higher than the value also sorted.")
        sub_case = ReadCase() # reads the case
        if sub_case == 1:
            value = ReadValue() # reads the value
            score_list = Less(score_list, value) # gets the list with values less than a value
        
        elif sub_case == 2:
            score_list = SortAllValues(score_list) # gets the list sorted
        
        elif sub_case == 3:
            value = ReadValue() # reads the value
            score_list = SortValuesGreater(score_list, value) # gets the scores greater than a value sorted
    
    elif case == 4:
        print("You chose to obtain different characteristics of the participants. If you insert 1 and two indexes, you will get the average score for the participants between the two given index, else if you insert 2 and two indexes, you will get the minimum score for participants between the two given index, else if you insert 3 a value and two indexes, you will get the score of participants between the two given index, which are multiples of the value.")
        sub_case = ReadCase() # reads the case
        if sub_case == 1:
            index1 = ReadIndex() # reads the index
            while index1 < 0 or index1 >= len(score_list):
                print("Wrong index!")
                index1 = ReadIndex() # reads the index
            index2 = ReadIndex() # reads the index
            while index2 < 0 or index2 >= len(score_list):
                print("Wrong index!")
                index2 = ReadIndex() # reads the index
            if index1 > index2:
                aux = index1
                index1 = index2
                index2 = aux
            PrintArray(SequenceAvg(score_list, index1, index2)) # prints the average score between two indexes
        
        elif sub_case == 2:
            index1 = ReadIndex() # reads the index
            while index1 < 0 or index1 >= len(score_list):
                print("Wrong index!")
                index1 = ReadIndex() # reads the index
            index2 = ReadIndex() # reads the index
            while index2 < 0 or index2 >= len(score_list):
                print("Wrong index!")
                index2 = ReadIndex() # reads the index
            PrintArray(SequenceMin(score_list, index1, index2)) # prints the minimum score between two indexes
            if index1 > index2:
                aux = index1
                index1 = index2
                index2 = aux
        elif sub_case == 3:
            value = ReadValue() # reads the value
            while value < 0 or value > 10:
                print("Wrong value!")
                value = ReadValue() # reads the value
            index1 = ReadIndex() # reads the index
            while index1 < 0 or index1 >= len(score_list):
                print("Wrong index!")
                index1 = ReadIndex() # reads the index
            index2 = ReadIndex() # reads the index
            while index2 < 0 or index2 >= len(score_list):
                print("Wrong index!")
                index2 = ReadIndex() # reads the index
            if index1 > index2:
                aux = index1
                index1 = index2
                index2 = aux
            PrintArray(SequenceMul(score_list, value, index1, index2)) # prints the scores multiple of a value between two indexes
    
    elif case == 5:
        prev_score_list = score_list.copy()
        print("You chose to filter the values. If you insert 1 and a value, you will get the list with only the participants with scores multiple of value, else if you insert 2 and a value you will get the list only with participants with scores higher than value.")
        sub_case = ReadCase() # reads the case
        if sub_case == 1:
            value = ReadValue() # reads the value
            while value < 0 or value > 10:
                print("Wrong value!")
                value = ReadValue() # reads the value
            score_list = FilterMul(score_list, value) # gets the scores multiple of a value
        
        elif sub_case == 2:
            value = ReadValue() # reads the value
            while value < 0 or value > 10:
                print("Wrong value!")
                value = ReadValue() # reads the value
            score_list = FilterGreater(score_list, value) # gets the scores greater than a value
    
    elif case == 6:
        print("You chose to undo the last operation that modified the array.")
        score_list = Undo(prev_score_list, score_list) # undos the last opertation that modified the array    
    elif case == 7:
        print("You chose to print the array.")
        PrintArray(score_list) # prints the array
    
    print(Message())
    case = ReadCase() # reads the case
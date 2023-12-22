from utilities.undo import Undo

def TestUndo():
    old_score_list = [1, 2, 3]
    current_score_list = [1, 2, 3]
    assert Undo(old_score_list, current_score_list) == [1, 2, 3]
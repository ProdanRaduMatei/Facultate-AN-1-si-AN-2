from utilities.sequence_min import SequenceMin

def TestSequenceMin():
    score_list = [5]
    min = SequenceMin(score_list, 0, 0)
    assert min == 5
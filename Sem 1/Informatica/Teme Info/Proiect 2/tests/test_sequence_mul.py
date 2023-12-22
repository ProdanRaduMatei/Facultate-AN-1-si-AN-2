from utilities.sequence_mul import SequenceMul

def TestSequenceMul():
    score_list = [5]
    mul = SequenceMul(score_list, 5, 0, 0)
    assert mul == [5]
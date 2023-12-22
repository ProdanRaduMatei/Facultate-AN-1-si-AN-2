from utilities.sequence_avg import SequenceAvg

def TestSequenceAvg():
    score_list = [5]
    avg = SequenceAvg(score_list, 0, 0)
    assert avg == 5.0
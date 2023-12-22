from tests.test_add import TestAdd
from tests.test_filter_greater import TestFilterGreater
from tests.test_filter_mul import TestFilterMul
from tests.test_insert import TestInsert
from tests.test_less import TestLess
from tests.test_print_array import TestPrintArray
from tests.test_remove_element import TestRemoveElement
from tests.test_remove_interval import TestRemoveInterval
from tests.test_replace import TestReplace
from tests.test_sequence_avg import TestSequenceAvg
from tests.test_sequence_min import TestSequenceMin
from tests.test_sequence_mul import TestSequenceMul
from tests.test_sorted1 import TestSortAllValues
from tests.test_sorted2 import TestSortValuesGreater
from tests.test_undo import TestUndo

def RunAllTests():
    if (TestAdd() == False):
        print("TestAdd failed!")
    if (TestFilterGreater() == False):
        print("TestFilterGreater failed!")
    if (TestFilterMul() == False):
        print("TestFilterMul failed!")
    if (TestInsert() == False):
        print("TestInsert failed!")
    if (TestLess() == False):
        print("TestLess failed!")
    if (TestPrintArray() == False):
        print("TestPrintArray failed!")
    if (TestRemoveElement() == False):
        print("TestRemoveElement failed!")
    if (TestRemoveInterval() == False):
        print("TestRemoveInterval failed!")
    if (TestReplace() == False):
        print("TestReplace failed!")
    if (TestSequenceAvg() == False):
        print("TestSequenceAvg failed!")
    if (TestSequenceMin() == False):
        print("TestSequenceMin failed!")
    if (TestSequenceMul() == False):
        print("TestSequenceMul failed!")
    if (TestSortAllValues() == False):
        print("TestSortAllValues failed!")
    if (TestSortValuesGreater() == False):
        print("TestSortValuesGreater failed!")
    if (TestUndo() == False):
        print("TestUndo failed!")
    print("All tests passed!")

from lib.counter import *

def test_counter_add_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == f"Counted to 5 so far."
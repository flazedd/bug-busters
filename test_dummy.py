from dummy import Dummy

def test_add():
    dummy = Dummy()
    assert dummy.add(2, 3) == 5

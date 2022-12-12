from _1_pytest import fun

def test_add_int():
    assert fun(3,1) == 4

def test_add_str():
    assert fun('a','b') == 'ab'

class TestDemo:
    def test_add_int(self):
        assert fun(3,1) == 4

    def test_add_str(self):
        assert fun('a','b') == 'ab'
    


    
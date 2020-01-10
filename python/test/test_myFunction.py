from myFunction import multiply

def multiply_by_zero():
    assert multiply(0,0) == 0

def test_multiply_by_1():
    assert multiply(1,1) == 1

from problems.strings import reverse


def test_reverse1():
    assert reverse.reverse1('1abcd2') == '2dcba1'

def test_reverse2():
    assert reverse.reverse2('1abcd2') == '2dcba1'

def test_reverse3():
    assert reverse.reverse3('1abcd2') == '2dcba1'


def test_reverse3():
    assert reverse.reverse4('1abcd2') == '2dcba1'
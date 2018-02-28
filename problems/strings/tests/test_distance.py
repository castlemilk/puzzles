from problems.strings import distance


def test_distance_LD():
    # recursive solution
    assert distance.LD('cat', 'dog') == 3
    assert distance.LD('abcd', 'abcd2') == 1
    assert distance.LD('abcdefgf', 'haabdecd2') == 6


def test_distance_VLD():
    # recursive solution
    assert distance.VLD('cat', 'dog') == 3




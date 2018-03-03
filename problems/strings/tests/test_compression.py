from problems.strings import compression


def test_compression():
    # recursive solution
    assert compression.compress('aaaa') == 'a4'
    assert compression.compress('aaaabbb') == 'a4b3'
    assert compression.compress('aaaabbbww') == 'a4b3w2'
    assert compression.compress('aaaabbbwwnnnnnnneeee') == 'a4b3w2n7e4'
    assert compression.compress('abcde') == 'abcde'
    assert compression.compress('abcccccccccde') == 'a1b1c9d1e1'




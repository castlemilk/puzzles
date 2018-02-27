from problems.strings import substrings


def test_permutations1():
    assert substrings.is_permutation('abcd','aaaaa') is False
    assert substrings.is_permutation('abcd', 'dcab') is True
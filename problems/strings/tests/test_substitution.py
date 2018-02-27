from problems.strings import substitution


def test_substitution1():
    assert substitution.substitute('hello lol', ' ', '%20') == 'hello%20lol'
    assert substitution.substitute('https://this.is.some.domain/some silly choco url with spaces', ' ', '%20') \
        == 'https://this.is.some.domain/some%20silly%20choco%20url%20with%20spaces'

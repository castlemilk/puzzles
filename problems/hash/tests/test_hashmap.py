
from problems.hash.HashMap import HashMap
def test_hashMap1():
    d = HashMap()
    d.put(1, 20)
    d.put(2, 21)
    d.put(3, 22)
    d.put(4, 23)
    assert d.get(3) == 22
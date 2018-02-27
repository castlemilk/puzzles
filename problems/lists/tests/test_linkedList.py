from problems.lists.LinkedList1 import LinkedList


def test_hashMap1():
    d = LinkedList()
    d.add(1)
    d.add(2)
    d.add(3)
    d.add(4)
    assert d.size() == 4
    assert d.search(4).get_data() == 4
    d.remove(4)
    assert d.size() == 3
    d.add(4)
    d.add(5)
    d.add(6)


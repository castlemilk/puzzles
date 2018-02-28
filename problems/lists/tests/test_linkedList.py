from problems.lists.LinkedList1 import LinkedList1
from problems.lists.LinkedList2 import LinkedList2


def test_linkedList1():
    d = LinkedList1()
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
    assert d.size() == 6
    d.remove(4)
    d.remove(1)
    d.remove(3)
    d.remove(6)
    assert d.size() == 2


def test_linkedList1_duplicates():
    d = LinkedList1()
    d.add(1)
    d.add(2)
    d.add(3)
    d.add(3)
    d.add(4)
    d.add(5)
    assert d.size() == 6
    d.remove_duplicates()
    assert d.size() == 5


def test_linkedList2():
    d = LinkedList2()
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
    assert d.size() == 6
    d.remove(4)
    d.remove(1)
    d.remove(3)
    d.remove(6)
    assert d.size() == 2



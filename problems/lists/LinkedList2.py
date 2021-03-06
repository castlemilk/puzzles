class Node(object):
    """
    Node which contains the information about neighbor node etc
    This is a singly-linked node, where it only points/references the next node, not the previous
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return "| {} -> {} |".format(self.data, self.next)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class LinkedList2(object):
    """
    Simpler Singly-linked list implementation. Where there is only a reference to the next time in the list and not the previous

    head -> node -> node -> node -> node -> node -> None
    """

    def __init__(self):
        self.head = Node()

    def is_empty(self):
        return self.head is None

    def traversal(self, data=None):
        node = self.head
        index = 0
        found = False
        while node is not None and not found:
            if not data:
                print(node)
            if node.get_data() == data:
                found = True
            else:
                node = node.get_next()
                index += 1
        return node, index

    def size(self):
        _, count = self.traversal(None)
        return count

    def search(self, data):
        node, _ = self.traversal(data)
        return node

    def add(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def remove(self, data):
        previous_node = None
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.get_data() == data:
                found = True
                if previous_node:
                    previous_node.set_next(current_node.get_next())
                else:
                    previous_node = current_node.get_next()
                    self.head = previous_node

            else:
                previous_node = current_node
                current_node = current_node.get_next()

        return found

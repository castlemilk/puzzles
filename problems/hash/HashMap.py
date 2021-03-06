import sys


class HashMap(object):
    def __init__(self):
        self.SIZE_OF_TABLE = 128
        self.BIG_PRIME = 175365371
        self.table = [None] * self.SIZE_OF_TABLE

    def get(self, key):
        index = self.hashCode(key)
        if self.table[index]:
            for item in self.table[index]:
                if item.key == key:
                    return item.value

        raise Exception("no item found at key: {}".format(key))

    def put(self, key, value):
        index = self.hashCode(key)
        hash_entry = HashEntry(key, value)
        chain = self.table[index]
        if not chain:
            chain = []

        it = iter(chain)
        item_next = next(it, None)
        while (item_next):
            if item_next.key == key:
                chain.remove(item_next)
                break

        chain.append(hash_entry)
        self.table[index] = chain
        return True

    def hashCode(self, h):
        if h >= 0:
            return (h * self.BIG_PRIME) % self.SIZE_OF_TABLE
        else:
            return ((sys.maxsize - h) & self.BIG_PRIME) % self.SIZE_OF_TABLE


class HashEntry(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

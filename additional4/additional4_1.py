class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableDict:
    def __init__(self, cap=50):
        self.cap = cap
        self.size = 0
        self.n = 0
        self.b = 0
        self.buckets = [None] * self.cap

    def hash(self, key):
        return hash(key) % self.cap

    def get(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        previous = None
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            previous = node
            node = node.next

        if node is None:
            return None

        result = node.value

        if previous is None:
            self.buckets[index] = node.next
        else:
            previous.next = previous.next.next

        self.size -= 1
        return result

    def add(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        while node.next is not None:
            node = node.next

        node.next = Node(key, value)

    def size(self):
        return self.size

    def __next__(self):
        if self.n is not None:
            current = self.n
            self.n = self.n.next
            return current.key, current.value

        self.b += 1
        if self.b == self.cap:
            raise StopIteration
        self.n = self.buckets[self.b]

        return self.__next__()

    def __iter__(self):
        self.b = 0
        self.n = self.buckets[0]
        return self

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __len__(self):
        return self.size


def test_hash_table():
    table = HashTableDict()

    for i in range(1000):
        table[i] = i + 1
        assert table[i] == i + 1
        assert table[chr(i)] is None

    assert len(table) == 1000

    for key, value in table:
        print(str(key) + ': ' + str(value))


if __name__ == '__main__':
    test_hash_table()
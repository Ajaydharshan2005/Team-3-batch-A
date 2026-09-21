class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self._size += 1

    def traverse(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __iter__(self):
        return self.traverse()

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if isinstance(index, slice):
            return list(self)[index]

        if not isinstance(index, int):
            raise TypeError("LinkedList indices must be integers or slices")

        if index < 0:
            index += self._size

        if index < 0 or index >= self._size:
            raise IndexError("LinkedList index out of range")

        for position, data in enumerate(self.traverse()):
            if position == index:
                return data

        raise IndexError("LinkedList index out of range")

    def is_empty(self):
        return self._size == 0
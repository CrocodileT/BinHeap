import math

class BinHeap:
    # if max_in_head = True then max priority in head
    # else min priority
    def __init__(self, max_in_head=True):
        self.heap = list()
        self.max_in_head = max_in_head

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left_child(i):
        return 2 * i + 1

    @staticmethod
    def _right_child(i):
        return 2 * i + 2

    def head(self):
        return self.heap[0]

    def compare(self, ind1: int, ind2: int) -> bool:
        return self.heap[ind1] < self.heap[ind2] if self.max_in_head else self.heap[ind1] > self.heap[ind2]

    def swap(self, ind1: int, ind2: int) -> None:
        self.heap[ind1], self.heap[ind2] = self.heap[ind2], self.heap[ind1]

    def up(self, i):
        while i > 0 and self.compare(BinHeap._parent(i), i):
            self.swap(BinHeap._parent(i), i)
            i = BinHeap._parent(i)

    def down(self, i):
        index = i
        size = len(self.heap)

        left = BinHeap._left_child(i)
        if left < size and self.compare(index, left):
            index = left

        right = BinHeap._right_child(i)
        if right < size and self.compare(index, right):
            index = right

        if i != index:
            self.swap(i, index)
            self.down(index)

    def insert(self, priority):
        self.heap.append(priority)
        self.up(len(self.heap) - 1)

    def extract(self):
        result = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.down(0)
        return result

    def remove(self, i):
        self.heap[i] = math.inf if self.max_in_head else -math.inf
        self.up(i)
        self.extract()

    def change_priority(self, i, priority):
        old_p = self.heap[i]
        self.heap[i] = priority
        if priority > old_p:
            self.up(i)
        else:
            self.down(i)

    def build_heap(self, array):
        i = len(array) // 2
        self.heap = array[:]
        while i >= 0:
            self.down(i)
            i = i - 1

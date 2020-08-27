from heapq import heappush, heappop


class SlidingSortedList:
    def __init__(self):
        self.size = 0
        self.pivot = 0
        self.pos = 0
        self.minheap, self.maxheap = [], []

    def _increment(self):
        if not self.maxheap:
            raise IndexError
        heappush(self.minheap, self.pivot)
        self.pivot = -heappop(self.maxheap)
        self.pos += 1

    def _decrement(self):
        if not self.minheap:
            raise IndexError
        heappush(self.maxheap, -self.pivot)
        self.pivot = heappop(self.minheap)
        self.pos -= 1

    def __getitem__(self, index):
        while self.pos < index:
            self._increment()
        while self.pos > index:
            self._decrement()
        return self.pivot

    def insert(self, item):
        self.size += 1
        if item < self.pivot:
            heappush(self.minheap, item)
            self.pos += 1
        else:
            heappush(self.maxheap, -item)

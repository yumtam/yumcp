from heapq import heapify, heappop, heappush

class Heap(list):
    def __init__(self, iterable=(), key=lambda x: x):
        super(Heap, self).__init__()
        for x in iterable:
            self.append(x)
        heapify(self)
        self.keyfunc = key

    def push(self, item):
        key = self.keyfunc(item)
        heappush(self, (key, item))

    def pop(self):
        return heappop(self)

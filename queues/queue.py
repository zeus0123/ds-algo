class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def peek(self):
        return self._items[-1]
    
    def view(self):
        return self._items
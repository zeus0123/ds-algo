class Stack:
    '''Stack Impementation as a List'''

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def is_empty(self):
        return not bool(self._items)
    
    def pop(self):
        return self._items.pop()
    
    def peek(self):
        # This always confuses me but anyways -1 is to take a peek at the last item or the first item that was pushed right?
        return self._items[-1]
    
    def size(self):
        return len(self._items)
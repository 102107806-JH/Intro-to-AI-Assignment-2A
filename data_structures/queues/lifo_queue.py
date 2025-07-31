class Stack:
    def __init__(self):
        self._collection = []

    def push(self, object):
        self._collection.append(object)

    def pop(self):
        return self._collection.pop()

    def is_empty(self):
        return len(self._collection) == 0
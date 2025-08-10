class Stack:
    def __init__(self):
        self._collection = []  # The underlying collection of the stack #

    def push(self, object):
        self._collection.append(object)  # Append an object to the underlying collection #

    def pop(self):
        return self._collection.pop()  # Remove the most recently added element (LIFO) #

    def is_empty(self):
        return len(self._collection) == 0  # Bool indicating whether the queue is empty #
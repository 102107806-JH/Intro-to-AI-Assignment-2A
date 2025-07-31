
class PriorityQueue:
    def __init__(self, key_lambda):
        self._collection = []
        self._key_lambda = key_lambda

    def push(self, object):
        self._collection.append(object)
        self._collection = sorted(self._collection, key=self._key_lambda)

    def pop(self):
        return self._collection.pop(0)

    def is_empty(self):
        return len(self._collection) == 0
from collections import deque


class FifoQueue:

    def __init__(self):
        self._queue = deque()

    def append(self, item):
        self._queue.append(item)

    def popleft(self):
        if not self._queue:
            raise IndexError("pop from an empty queue")
        return self._queue.popleft()

    def __len__(self):
        return len(self._queue)

    def __bool__(self):
        return bool(self._queue)
from collections import deque

class FifoQueue:
    """
    A custom First-In, First-Out (FIFO) Queue.
    """
    def __init__(self):
        """
        Initializes an empty FIFO queue.
        Uses collections.deque for efficient operations.
        """
        self._queue = deque()

    def append(self, item):
        """
        Adds an item to the right end of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self._queue.append(item)

    def popleft(self):
        """
        Removes and returns an item from the left end (front) of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self._queue:
            raise IndexError("pop from an empty queue")
        return self._queue.popleft()

    def __len__(self):
        """
        Returns the number of items currently in the queue.
        Allows checking if the queue is empty using `if queue:`.
        """
        return len(self._queue)

    def __bool__(self):
        """
        Returns True if the queue is not empty, False otherwise.
        Allows checking if the queue is empty using `while queue:`.
        """
        return bool(self._queue)
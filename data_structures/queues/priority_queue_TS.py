import heapq


class PriorityQueue:

    def __init__(self):
        self._heap = []  # Initializes an empty list that heapq will manage as a min-heap.
        self._counter = 0  # Integer counter that increments with each push operation.

    def push(self, node):
        # Set the chronological order for tie-breaking
        node.order_pushed_into_collection = self._counter
        self._counter += 1

        # The tuple for heapq sorting is now:
        # (primary_priority, secondary_tie_breaker, tertiary_tie_breaker, actual_item_to_store)
        # 1. node.total_cost (f-value) - Primary priority
        # 2. node.state (smaller to bigger nodes) - Secondary tie-breaker (as requested)
        # 3. node.order_pushed_into_collection (chronological order) - Tertiary tie-breaker
        # 4. node (the actual Node object) - The item to be returned by pop
        heapq.heappush(self._heap, (node.total_cost, node.state, node.order_pushed_into_collection, node))

    def pop(self):
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        # The first three values are the sorting keys, the last one is the actual node.
        total_cost, node_state_id, order, node = heapq.heappop(self._heap)
        # We only need to return the 'node' object. The other unpacked variables can be ignored.
        return node

    def is_empty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def __bool__(self):
        return bool(self._heap)
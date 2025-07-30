# textbook_abstractions/node.py (MODIFIED)

class Node:
    # Class variable to keep track of the total number of Node instances created
    _node_count = 0

    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic_cost=0):
        self._state = state  # Node state #
        self._parent = parent  # Parent node #
        self._action = action  # Action that got the node from parent state to current node state #
        self._path_cost = path_cost  # Path cost will need to be saved whereas heuristic cost won't #
        self._total_cost = path_cost + heuristic_cost  # The total cost this is what the priority queue will sort by #

        # Increment the node count every time a new Node instance is created
        Node._node_count += 1

    @property
    def state(self):
        return self._state

    @property
    def parent(self):
        return self._parent

    @property
    def action(self):
        return self._action

    @property
    def path_cost(self):
        return self._path_cost

    @property
    def total_cost(self):
        return self._total_cost

    @staticmethod
    def get_node_count():
        """Returns the total number of Node instances created so far."""
        return Node._node_count

    @staticmethod
    def reset_node_count():
        """Resets the total number of Node instances created to 0."""
        Node._node_count = 0
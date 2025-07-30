class Node:
    def __init__(self, state, parent = None, action = None, path_cost = 0, heuristic_cost = 0):
        self._state = state  # Node state #
        self._parent = parent  # Parent node #
        self._action = action  # Action that got the node from parent state to current node state #
        self._path_cost = path_cost  # Path cost will need to be saved where as heuristic cost wont #
        self._total_cost = path_cost + heuristic_cost  # The total cost this is what the priority queue will sort by #

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
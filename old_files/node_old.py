class Node:
    # Class variable to keep track of the total number of Node instances created
    _node_count = 0

    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic_cost=0):
        self._state = state  # Node state
        self._parent = parent  # Parent node
        self._action = action  # Action that got the node from parent state to current node state
        self._path_cost = path_cost  # Path cost will need to be saved whereas heuristic cost won't
        self._heuristic_cost = heuristic_cost  # Make sure to store it as a private attribute
        self._total_cost = path_cost + heuristic_cost  # The total cost this is what the priority queue will sort by
        self._order_pushed_into_collection = None
        # Used to indicate chronological order in which node was added to a specific collection

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
    def heuristic_cost(self):
        return self._heuristic_cost

    @property
    def total_cost(self):
        return self._total_cost

    @property
    def order_pushed_into_collection(self):
        return self._order_pushed_into_collection

    @order_pushed_into_collection.setter
    def order_pushed_into_collection(self, order_pushed_into_collection):
        self._order_pushed_into_collection = order_pushed_into_collection

    @staticmethod
    def get_node_count():  # Returns the total number of Node instances created so far

        return Node._node_count

    @staticmethod
    def reset_node_count():  # Resets the total number of Node instances created to 0
        Node._node_count = 0

    def __lt__(self, other):
        # This method defines how one Node object is "less than" another
        # used by heapq in A* search when comparing the 3rd element of the tuple for Note 2 requirement
        if self.total_cost != other.total_cost:
            return self.total_cost < other.total_cost
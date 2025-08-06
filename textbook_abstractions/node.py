class Node:
    # Class variable to keep track of the total number of Node instances created
    _node_count = 0

    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic_cost=0, use_path_cost_for_total_cost = True, node_depth = 0):
        self._state = state  # Node state
        self._parent = parent  # Parent node
        self._action = action  # Action that got the node from parent state to current node state
        self._path_cost = path_cost  # Path cost will need to be saved whereas heuristic cost won't
        self._heuristic_cost = heuristic_cost # Make sure to store it as a private attribute
        self._use_path_cost_for_total_cost = use_path_cost_for_total_cost  # This is needed to signal whether the path cost is needed in the total cost later #
        self._node_depth = node_depth  # Node depth stored in the node so that it doesn't have to be calculated recursively #

        if use_path_cost_for_total_cost: # This is for gbfs where we want to record the path cost without using it in the total cost
            self._total_cost = path_cost + heuristic_cost  # The total cost this is what the priority queue will sort by
        else:
            self._total_cost = heuristic_cost
        self._order_pushed_into_collection = None  # Used to indicate chronological order in which node was added to a specific collection
        self._children = []  # Stores the child nodes #
        # Increment the node count every time a new Node instance is created
        Node._node_count += 1

    def update_subtree_cost(self, path_cost_difference):

        for child in self._children:  # Go through each of the children #
            child.path_cost -= path_cost_difference  # Update the path cost difference #

            if self._use_path_cost_for_total_cost:  # Check whether the path cost should be used in the total cost #
                child.total_cost -= path_cost_difference  # Subtract the difference in path cost from the total cost #

            child.update_subtree_cost(path_cost_difference)  # Recursive Call #

    def add_child(self, node):
        self._children.append(node)  # Appends a child to the children list of the node #

    def steal_children(self, old_node):
        self._children = old_node.children  # Update the children #
        old_node.children = []  # Set the old nodes children to an empty list #

        for child in self._children: # Go through every child #
            child.parent = self  # Make this object the parent of every child #

    @property
    def children(self):
        return self._children  # Get children list #

    @children.setter
    def children(self, children):
        self._children = children  # Set children list #

    @property
    def state(self):
        return self._state

    @property
    def node_depth(self):
        return self._node_depth

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent  # Set the parent of self #

    @property
    def action(self):
        return self._action

    @property
    def path_cost(self):
        return self._path_cost

    @path_cost.setter
    def path_cost(self, path_cost):
        self._path_cost = path_cost  # Set the path cost #

    @property
    def heuristic_cost(self):
        return self._heuristic_cost

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        self._total_cost = total_cost  # Set the total cost #

    @property
    def order_pushed_into_collection(self):
        return self._order_pushed_into_collection

    @order_pushed_into_collection.setter
    def order_pushed_into_collection(self, order_pushed_into_collection):
        self._order_pushed_into_collection = order_pushed_into_collection

    @staticmethod
    def get_node_count():
        """Returns the total number of Node instances created so far."""
        return Node._node_count

    @staticmethod
    def reset_node_count():
        """Resets the total number of Node instances created to 0."""
        Node._node_count = 0

    def __lt__(self, other):
        # This method defines how one Node object is "less than" another.
        # It's used by heapq in A* search when comparing the 3rd element of the tuple for Note 2 requirement.
        if self.total_cost != other.total_cost:
            return self.total_cost < other.total_cost
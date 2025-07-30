class Node:
    def __init__(self, state, parent = None, action = None, path_cost = 0, heuristic_cost = 0):
        self.state = state  # Node state #
        self.parent = parent  # Parent node #
        self.action = action  # Action that got the node from parent state to current node state #
        self.path_cost = path_cost  # Path cost will need to be saved where as heuristic cost wont #
        self.total_cost = path_cost + heuristic_cost  # The total cost this is what the priority queue will sort by #
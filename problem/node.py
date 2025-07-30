class Node:
    def __init__(self, state, parent = None, action = None, path_cost = 0, heuristic_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost # Path cost may need to be saved where as heuristic cost wont
        self.total_cost = path_cost + heuristic_cost
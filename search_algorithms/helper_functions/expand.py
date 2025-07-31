from textbook_abstractions.node import Node

def expand(problem, node):

    state = node.state  # The state of the parent node #
    children = []  # List to store all the child nodes #

    for action in problem.actions(state):  # Go through all the states #

        new_state = problem.result(state, action)  # Get the state that results from an action #
        cost = node.path_cost + problem.action_cost(state, action, new_state)  # Get the path cost to the current node #
        children.append(Node(state=new_state, parent=node, action=action, path_cost=cost))  # Append a new child node using the node constructor #

    return children
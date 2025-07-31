from textbook_abstractions.node import Node

def expand(problem, node):
    state = node.state
    children = []

    for action in problem.actions(state):
        new_state = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(state, action, new_state)
        children.append(
            Node(state=new_state, parent=node, action=action, path_cost=cost))

    return children
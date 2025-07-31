from data_structures.queues.priority_que_JH import PriorityQueue
from textbook_abstractions.node import Node

def greed_best_first_search(problem):
    node = Node(state=problem.initial_state)
    frontier = PriorityQueue(key_lambda=lambda node:(node.total_cost, node.state))
    frontier.push(node)
    reached = {problem.initial_state : True}

    while frontier.is_empty() == False:

        node = frontier.pop()

        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            state = child.state

            if reached.get(state, False) == False:
                reached[state] = True
                frontier.push(child)

    return None

def expand(problem, node):

    state = node.state  # The state of the parent node #
    children = []  # List to store all the child nodes #

    for action in problem.actions(state):  # Go through all the states #
        new_state = problem.result(state, action)  # Get the state that results from an action #
        heuristic_cost = problem.state_distance_to_goal(new_state)
        children.append(Node(state=new_state, parent=node, action=action, path_cost=0, heuristic_cost=heuristic_cost))  # Append a new child node using the node constructor #

    return children
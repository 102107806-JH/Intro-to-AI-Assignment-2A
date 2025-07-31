from textbook_abstractions.problem import Problem
from textbook_abstractions.node import Node
from data_structures.queues.lifo_queue import Stack
from search_algorithms.helper_functions.node_depth import node_depth
from search_algorithms.helper_functions.cycle_checker import is_cycle

def depth_first_search(problem, depth_limit, cycle_depth_limit):
    frontier = Stack()  # Frontier stack #
    frontier.push(Node(state=problem.initial_state))  # Push the initial node onto the stack #

    while frontier.is_empty() == False:  # Keep going until the frontier is empty #
        node = frontier.pop()  # Pop the top of the stack off #
        if problem.is_goal(node.state):  # If we are at the goal node return the node #
            return node

        if node_depth(node) < depth_limit and is_cycle(node, cycle_depth_limit) == False:  # Only enable expansion if the node is less than depth limit. Nodes at the depth limit will still be explored. Also check for cycles #

            for child in sorted(expand(problem, node), key=lambda node:node.state, reverse=True):  # Children need to be explored in
                # ascending order because stack is used need to push higher nodes first thus list needs reversing by state #
                frontier.push(child)  # Push child onto the frontier #

    return None  # No solution has been found #

def expand(problem, node):
    state = node.state  # The state of the parent node #
    children = []  # List to store all the child nodes #

    for action in problem.actions(state):  # Go through all the states #
        new_state = problem.result(state, action)  # Get the state that results from an action #
        children.append(Node(state=new_state, parent=node, action=action))  # Append a new child node using the node constructor #

    return children












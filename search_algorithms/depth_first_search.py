from textbook_abstractions.problem import Problem
from search_algorithms.helper_functions.expand import expand
from textbook_abstractions.node import Node
from data_structures.queues.lifo_queue import Stack
from search_algorithms.helper_functions.node_depth import node_depth

def depth_first_search(problem, expansion_depth_limit):
    frontier = Stack()
    frontier.push(Node(state=problem.initial_state))
    result = None

    while frontier.is_empty() == False:

        node = frontier.pop()

        if problem.is_goal(node.state):
            return node

        if node_depth(node) > expansion_depth_limit:
            result = "depth limit reach"
        else:
            for child in sorted(expand(problem, node), key=lambda node:node.state, reverse=True):
                frontier.push(child)

    return result












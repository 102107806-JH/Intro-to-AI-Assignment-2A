from textbook_abstractions.problem import Problem
from search_algorithms.helper_functions.expand import expand
from textbook_abstractions.node import Node
from data_structures.queues.lifo_queue import Stack

def depth_first_search(problem, depth):
    frontier = Stack()
    frontier.push(Node(state=problem.initial_state))
    result = None



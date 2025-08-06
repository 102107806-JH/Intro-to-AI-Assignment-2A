from textbook_abstractions.node import Node
from textbook_abstractions.problem import Problem
from data_structures.queues.priority_queue_TS import PriorityQueue
from search_algorithms.helper_functions.expand import expand


def dijkstra_search(problem: Problem):

    # f(n) = g(n).
    initial_node = Node(
        state=problem.initial_state,
        path_cost=0,
        heuristic_cost=0
    )

    # The frontier is a priority queue, ordered by f(n) = g(n).
    # Ties are broken by node.state, then by chronological order.
    frontier = PriorityQueue()
    frontier.push(initial_node)

    # Dictionary to store the lowest g(n) found so far
    # for each state encountered.
    cost_so_far = {initial_node.state: initial_node.path_cost}

    explored_states = set()

    while frontier:
        current_node = frontier.pop()

        if current_node.state in explored_states:
            continue

        # If the current node is a goal state, an optimal path has been found.
        if problem.is_goal(current_node.state):
            return current_node

        # Add the current node's state to the set of explored states.
        explored_states.add(current_node.state)

        # Expand the current node to generate its children.
        for child_node in expand(problem, current_node):

            # heuristic_cost is not part of the search priority.
            child_node._heuristic_cost = 0
            child_node._total_cost = child_node.path_cost

            # Check if this new path is better than any previously found path to this state.
            if child_node.state not in cost_so_far or \
                    child_node.path_cost < cost_so_far[child_node.state]:

                cost_so_far[child_node.state] = child_node.path_cost

                frontier.push(child_node)

    # If the frontier becomes empty and no goal is found, return None.
    return None
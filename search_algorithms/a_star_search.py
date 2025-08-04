from textbook_abstractions.node import Node
from textbook_abstractions.problem import Problem
from data_structures.queues.priority_queue_TS import PriorityQueue
from search_algorithms.helper_functions.expand import expand


def a_star_search(problem: Problem):
    """
    Performs an A* search to find an optimal path from the initial state
    to a goal state. This implementation uses a graph search approach.

    A* search algorithm formula was used from Page 72 of the textbook.
    f(n) = g(n) + h(n) where:
    g(n) is the path cost from the start node to node n.
    h(n) is an admissible heuristic estimate of the cost from node n to the closest goal.
    """

    # Create the initial node.
    # Its path_cost (g(n)) is 0.
    # Its heuristic_cost (h(n)) is calculated using the problem's heuristic function.
    initial_node = Node(
        state=problem.initial_state,
        path_cost=0,
        heuristic_cost=problem.state_distance_to_goal(problem.initial_state)
    )

    # The frontier is a priority queue, ordered by f(n) = g(n) + h(n).
    # Ties are broken by node.state (smaller ID first), then by chronological order.
    frontier = PriorityQueue()
    frontier.push(initial_node)

    # cost_so_far (g-scores): A dictionary is used to store the lowest g(n) found so far
    # for each state encountered.
    cost_so_far = {initial_node.state: initial_node.path_cost}

    # explored_states: A set of states that have already been expanded (popped
    # from the frontier and had their children generated). This prevents
    # re-expanding already-optimal paths.
    explored_states = set()

    while frontier:  # Loop while the frontier is not empty
        current_node = frontier.pop()  # Get the node with the lowest f(n)

        # If the current node's state has already been fully explored through an
        # equal or better path, then skip.
        if current_node.state in explored_states:
            continue

        # If the current node is a goal state, an optimal path has been found.
        if problem.is_goal(current_node.state):
            return current_node

        # Add the current node's state to the set of explored states.
        explored_states.add(current_node.state)

        # Expand the current node to generate its children.
        for child_node in expand(problem, current_node):
            # child_node.path_cost is the g(n) for this path to the child.

            # Check if this child state has been encountered before,
            # and if the new path to it is better (lower g(n)).
            if child_node.state not in cost_so_far or \
                    child_node.path_cost < cost_so_far[child_node.state]:

                # Update the best known cost to this state.
                cost_so_far[child_node.state] = child_node.path_cost

                # Push the child node onto the priority queue.
                # The PriorityQueue handles setting _order_pushed_into_collection
                # and uses it for tie-breaking.
                frontier.push(child_node)

    # If the frontier becomes empty and no goal is found, return None.
    return None
from collections import deque
from textbook_abstractions.node import Node


def breadth_first_search(problem):
    """
    Breadth-First Search (BFS) to find a destination node or failure

    Args:
        problem: An instance of the Problem class, containing the initial state,
                 goal states, and methods for actions, result, and goal checking.

    Returns:
        A Node object representing the solution path if a goal (destination) is found,
        otherwise None.
    """

    # Create the initial node using the problem's initial state
    node = Node(problem.initial_state)

    # Check if the initial state is already a goal state
    if problem.is_goal(node.state):
        return node

    # Initialize the frontier as a deque FIFO operation
    frontier = deque([node])

    # Record states that have been reached to avoid cycles and redundant processing
    reached = {problem.initial_state}

    while frontier:
        # Get the next node from the front of the queue
        current_node = frontier.popleft()

        # Expand the current node to generate child nodes
        for action in problem.actions(current_node.state):
            child_state = problem.result(current_node.state, action)  # Get the result of the action
            cost_to_child = problem.action_cost(current_node.state, action, child_state)  # Get the cost of the action
            child_path_cost = current_node.path_cost + cost_to_child  # Calculate the path cost of the child node
            # Create a new child node and update the current params
            child_node = Node(
                state=child_state,
                parent=current_node,
                action=action,
                path_cost=child_path_cost
            )

            # Check if the child state is a goal
            if problem.is_goal(child_node.state):
                return child_node

            # if s is not in reached then
            # Check if the child state has already been reached
            if child_node.state not in reached:
                # add s to reached
                reached.add(child_node.state)
                # add child to frontier
                frontier.append(child_node)

    # return failure
    # If the frontier becomes empty and no goal is found, return None
    return None
from textbook_abstractions.node import Node
from data_structures.queues.fifo_queue import FifoQueue


def breadth_first_search(problem):
    """
    Performs a Breadth-First Search (BFS) to find a solution node or failure.

    Args:
        problem: An instance of the Problem class, containing the initial state,
                 goal states, and methods for actions, result, and goal checking.

    Returns:
        A Node object representing the solution path if a goal is found,
        otherwise None.
    """
    node = Node(problem.initial_state)

    if problem.is_goal(node.state):
        return node

    # Initialize the frontier using the custom FifoQueue
    frontier = FifoQueue()  # Use custom FifoQueue
    frontier.append(node)  # Add the initial node

    reached = {problem.initial_state}

    while frontier: # This now works due to __bool__ method in FifoQueue
        current_node = frontier.popleft()  # Use popleft from custom queue
        # Check if the current node is a goal if not return the path
        for action in problem.actions(current_node.state):
            child_state = problem.result(current_node.state, action)
            cost_to_child = problem.action_cost(current_node.state, action, child_state)
            child_path_cost = current_node.path_cost + cost_to_child

            child_node = Node( # Create a new node and set/update attributes
                state=child_state,
                parent=current_node,
                action=action,
                path_cost=child_path_cost
            )
            # Check if the child node is a goal or not
            if problem.is_goal(child_node.state):
                return child_node
            # Check if the child node is already in the queue or not
            if child_node.state not in reached:
                reached.add(child_node.state)
                frontier.append(child_node)

    return None
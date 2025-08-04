from textbook_abstractions.node import Node


def expand(problem, parent_node):
    """
    Generates and returns a list of child Node objects for a given parent node.
    This function calculates g(n) and h(n) for each child, which are then used
    to set the child's path_cost and heuristic_cost, respectively.
    """
    children = []
    # problem.actions() returns actions (which are state IDs) sorted in ascending order for NOTE 2 Requirement
    for action_state_id in problem.actions(parent_node.state):
        # Calculate g(n) for the child: parent's path_cost + cost of current action
        step_cost = problem.action_cost(parent_node.state, action_state_id, action_state_id)
        new_path_cost = parent_node.path_cost + step_cost

        # Calculate h(n) for the child: heuristic estimate to the closest goal
        # This uses the state_distance_to_goal heuristic from the Problem class
        heuristic_cost = problem.state_distance_to_goal(action_state_id)

        # Create the new child Node
        child_node = Node(
            state=action_state_id,
            parent=parent_node,
            action=action_state_id,  # In this problem, action is equivalent to the next state ID
            path_cost=new_path_cost,
            heuristic_cost=heuristic_cost  # This sets node.total_cost (f(n)) implicitly
        )
        children.append(child_node)

    return children
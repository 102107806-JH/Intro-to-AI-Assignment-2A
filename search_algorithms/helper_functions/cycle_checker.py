def is_cycle(node, cycle_depth_limit):
    current_node = node.parent  # Go one node up in the tree #

    while cycle_depth_limit > 0 and current_node is not None:
        # Keep going up nodes in the tree until the cycle depth limit is reached, or you run out of nodes

        if node.state == current_node.state:  # A cycle has been found #
            return True

        cycle_depth_limit -= 1  # Decrement depth limit #
        current_node = current_node.parent  # Move up the tree #

    return False
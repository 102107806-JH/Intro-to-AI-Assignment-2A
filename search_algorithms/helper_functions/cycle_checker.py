def is_cycle(node, cycle_depth_limit):
    current_node = node.parent

    while cycle_depth_limit > 0 and current_node is not None:

        if node.state == current_node.state:
            return True

        cycle_depth_limit -= 1
        current_node = current_node.parent



    return False


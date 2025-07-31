def node_depth(node):
    depth = 0  # Initial depth of 0 #

    # Go back upto the head of the tree incrementing the counter at each step
    while node.parent is not None:

        depth += 1
        node = node.parent

    return depth  # Return the depth #

def node_depth(node):
    depth = 0

    while node.parent is not None:
        depth += 1
        node = node.parent

    return depth
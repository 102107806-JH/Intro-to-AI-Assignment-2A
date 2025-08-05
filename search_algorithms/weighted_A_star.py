from data_structures.queues.priority_que_JH import PriorityQueue
from textbook_abstractions.node import Node

def weighted_A_star(problem, weight=1):
    node = Node(state=problem.initial_state)  # Initial node #
    frontier = PriorityQueue(key_lambda=lambda node:(node.total_cost, node.state))  # Frontier that takes the lambda as an arg that defines how the priority queue is sorted. In this case we dont need to worry about sorting by chronological order because it is impossible for the same state to occur twice #
    frontier.push(node)  # Push initial node onto the queue #
    reached = {problem.initial_state : node}  # Dictionary that stores the reached state states #

    while frontier.is_empty() == False:  # Continue until frontier is empty #
        node = frontier.pop()  # Pop the highest priority node #

        if problem.is_goal(node.state):  # Check to see if the goal has been found #
            return node

        for child in expand(problem, node, weight):  # Expand popped nodes children #
            state = child.state  # Get the state of the current child #

            if state not in reached or child.path_cost < reached[state].path_cost:  # Make sure that the frontier nodes have not been encountered before pushing them onto frontier OR if they have been encountered check if the current path costs less #

                if state in reached:  # The node is in reached this means that the path cost is less on the newly found node #
                    update_tree(new_node=child, old_node=reached[state])  # Calls the function that is responsible for updating the tree #
                else:
                    frontier.push(child)  # Push node onto frontier (Nodes can only appear on the frontier once) #
                    node.add_child(child)  # Add child to the node #

                reached[state] = child  # Indicate that the node has been reached OR update the node for one that has the better path cost #

    return None

def expand(problem, node, weight):
    state = node.state  # The state of the parent node #
    children = []  # List to store all the child nodes #

    for action in problem.actions(state):  # Go through all the states #
        new_state = problem.result(state, action)  # Get the state that results from an action #
        path_cost = node.path_cost + problem.action_cost(state, action, new_state)  # Get the total cost of the action plus all previous actions taken #
        heuristic_cost = weight * problem.state_distance_to_goal(new_state)  # Get the heuristic (straight line distance) for the expanded node and multiply it by the weight
        children.append(Node(state=new_state, parent=node, action=action, path_cost=path_cost, heuristic_cost=heuristic_cost))  # Append a new child node using the node constructor. #

    return children

def update_tree(new_node, old_node):
    new_node.steal_children(old_node)  # Steals the old nodes children and sets the new node as their parent. Then sets the old nodes children to none #
    new_node.update_subtree_cost(path_cost_difference=old_node.path_cost - new_node.path_cost)  # Updates the cost of all the nodes on the subtree #

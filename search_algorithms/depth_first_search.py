from textbook_abstractions.problem import Problem
from textbook_abstractions.node import Node
from data_structures.queues.lifo_queue import Stack
from search_algorithms.helper_functions.node_depth import node_depth

def depth_first_search(problem, depth_limit):
    frontier = Stack()  # Frontier stack #
    frontier.push(Node(state=problem.initial_state))  # Push the initial node onto the stack #
    observed_states = {problem.initial_state : True}  # Dictionary for checking cycles in this problem the same state should never be encountered again #

    while frontier.is_empty() == False:  # Keep going until the frontier is empty #

        node = frontier.pop()  # Pop the top of the stack off #

        if problem.is_goal(node.state):  # If we are at the goal node return the node #
            return node

        if node_depth(node) < depth_limit:  # Only enable expansion if the node is less than or equal to expansion depth limit
            #  Nodes at the depth limit WILL BE EXPLORED JUST NOT EXPANDED #

            for child in sorted(expand(problem, node), key=lambda node:node.state, reverse=True):  # Children need to be explored in
                # ascending order because stack is used need to push higher nodes first thus list needs reversing by state #

                # Only push the child if that state has never been on the frontier before
                if observed_states.get(child.state, False) == False:
                    frontier.push(child)  # Push child onto the frontier #
                    observed_states[child.state] = True  # The pushed child has been on the frontier so indicate this in the dictionary #

    return None  # No solution has been found #

def expand(problem, node):

    state = node.state  # The state of the parent node #
    children = []  # List to store all the child nodes #

    for action in problem.actions(state):  # Go through all the states #

        new_state = problem.result(state, action)  # Get the state that results from an action #
        children.append(Node(state=new_state, parent=node, action=action))  # Append a new child node using the node constructor #

    return children












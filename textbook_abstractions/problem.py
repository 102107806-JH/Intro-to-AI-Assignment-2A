class Problem:
    def __init__(self, extracted_text_file_data_object):  # Takes an extracted text file object  #
        self._graph = extracted_text_file_data_object.adjacency_list_graph  # Store a reference to the graph  #
        self._initial_state = extracted_text_file_data_object.origin  # Store the initial state (int) #
        self._goal_states = extracted_text_file_data_object.destinations_list  # List of the goal states (int) #

    @property
    def initial_state(self):
        return self._initial_state

    def actions(self, state):  # Gives the actions that are available in current state #
        destination_cost_pair_list = self._graph.get_edge_data(state)  # Gets a list of the destination cost pair
        # objects for the current state #
        actions_list = []  # We are only interested in the actions not the cost #

        # Extract the actions from the pairs #
        for pair in destination_cost_pair_list:
            actions_list.append(pair.destination_id)

        actions_list.sort()  # Sort actions in ascending order #

        return actions_list  # Returns a list of integers each representing a state that can be reached
        # from the current state #

    def result(self, state, action):  # Returns the result of performing an action on a state.
        # State is unneeded but included to remain consistent with the book #
        return action  # The action is an integer representing the destination node.
        # This can be directly returned because it is the next state #

    def action_cost(self, state, action, new_state):
        destination_cost_pair_list = self._graph.get_edge_data(state)  # Get all destinations and their costs
        # associated with current state #

        for pair in destination_cost_pair_list:  # Go through all the pairs in the cost pair list #
            if pair.destination_id == new_state:  # The destination and the new state match #
                return pair.cost  # Return the cost associated with the pair

        return None  # There is no match this should never happen #

    def state_distance_to_goal(self, state):

    def is_goal(self, state):
        return state in self._goal_states  # Seeing if the state is in the goal states #

    def get_graph_diameter(self):
        return self._graph.get_graph_diameter()  # Calls the graphs diameter function to get the diameter #
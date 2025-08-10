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
        best_cost = float('inf')  # Could have multiple paths to the same destination from a given state #
        for pair in destination_cost_pair_list:  # Go through all the pairs in the cost pair list #
            if pair.destination_id == new_state:  # The destination and the new state match #
                best_cost = min(best_cost, pair.cost)  # Get the best cost path to the destination #

        if best_cost != float('inf'):
            return best_cost  # Return the best cost #
        else:
            raise Exception('Invalid action no resulting state!')  # There is no match this should never happen #

    def state_distance_to_goal(self, state):
        state_vertex = self._graph.id_to_vertex(state)  # Get the vertex of the input state #
        min_distance = float('inf')  # Set the distance at infinity #

        for goal_state in self._goal_states:  # Go through all the goal states #

            goal_vertex = self._graph.id_to_vertex(goal_state)
            cur_distance = ((goal_vertex.x - state_vertex.x) ** 2 + (goal_vertex.y - state_vertex.y) ** 2) ** 0.5
            # Calculate the Euclidean (straight line) distance to given goal for the state #
            min_distance = min(min_distance, cur_distance)  # Getting the distance to the closest goal #

        return min_distance

    def is_goal(self, state):
        return state in self._goal_states  # Seeing if the state is in the goal states #

    def get_graph_diameter(self):
        return self._graph.get_graph_diameter()  # Calls the graphs' diameter function to get the diameter #
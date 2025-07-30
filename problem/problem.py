from problem.node import Node

class Problem:
    def __init__(self, extracted_text_file_data_object):
        self._graph = extracted_text_file_data_object.adjacency_list_graph
        self._initial_state = Node(state=extracted_text_file_data_object.origin)
        self._goal_states = extracted_text_file_data_object.destinations_list

    def actions(self, state):
        destination_cost_pair_list = self._graph.get_edge_data(state)
        actions_list = []
        for pair in destination_cost_pair_list:
            actions_list.append(pair.destination_id)
        return actions_list

    def result(self, state, action):
        return action

    def action_cost(self, state, action, new_state):
        destination_cost_pair_list = self._graph.get_edge_data(state)

        for pair in destination_cost_pair_list:
            if pair.destination_id == new_state:
                return pair.cost
        return None


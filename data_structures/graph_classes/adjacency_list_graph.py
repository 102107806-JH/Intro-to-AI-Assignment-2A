from data_structures.graph_classes.vertex import Vertex
from data_structures.graph_classes.destination_cost_pair import DestinationCostPair

class AdjacencyListGraph:
    def __init__(self):
        self._adjacency_list = []  # Stores all the graph vertices #

    def insert_vertex(self, id, x, y):  # Insert another vertex into adjacency list #
        self._adjacency_list.append(Vertex(id, x, y))  # Calling the vertex constructor #

    def insert_edge_into_vertex(self, origin_id, destination_id, cost):  # Insert another edge for the origin_id #
        vertex = self._id_to_vertex(origin_id)  # Obtain the vertex specified by the origin id #
        vertex.add_edge(DestinationCostPair(destination_id, cost))  # Destination cost pair constructor #


    def get_edge_data(self, origin_id):  # Extract the edge data for a given origin vertex #
        vertex = self._id_to_vertex(origin_id)  # Get the vertex corresponding to the origin id #
        return vertex.edges  # Returns a list of the edges #

    def _id_to_vertex(self, id):
        return self._adjacency_list[id - 1] # Converting the vertex id into a list index. The id is 1 base so -1 to get it to zero based






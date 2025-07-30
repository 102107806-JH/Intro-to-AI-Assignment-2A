from data_structures.graph_classes.vertex import Vertex
from data_structures.graph_classes.destination_cost_pair import DestinationCostPair

class AdjacencyListGraph:
    def __init__(self):
        self._adjacency_list = [] # This stores objects of class vertex

    def insert_vertex(self, id, x, y):
        self._adjacency_list.append(Vertex(id, x, y))

    def insert_edge_into_vertex(self, origin_id, destination_id, cost):
        self._id_to_vertex(origin_id).add_edge(DestinationCostPair(destination_id, cost))

    def get_edge_data(self, origin_id):
        vertex = self._id_to_vertex(origin_id)
        return vertex.extract_edges_as_list()

    def _id_to_vertex(self, id):
        return self._adjacency_list[id - 1] # Converting the vertex id into a list index. The id is 1 base so -1 to get it to zero based






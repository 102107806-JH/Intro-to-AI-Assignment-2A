from data_structures.graph_classes.vertex import Vertex
from data_structures.graph_classes.destination_cost_pair import DestinationCostPair

class AdjacencyListGraph:
    def __init__(self):
        self._adjacency_list = [] # This stores objects of class vertex

    def insert_vertex(self, id, x, y):
        self._adjacency_list.append(Vertex(id, x, y))

    def insert_edge_into_vertex(self, origin_id, destination_id, cost):
        list_index = origin_id - 1 # Converting the vertex id into a list index. The id is 1 base so -1 to get it to zero based
        self._adjacency_list[list_index].add_edge(DestinationCostPair(destination_id, cost))


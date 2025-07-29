from data_structures.graph_classes.vertex import Vertex

class AdjacencyListGraph:
    def __init__(self):
        self._adjacency_list = [] # This stores objects of class vertex

    def insert_vertex(self, id, x, y):
        self._adjacency_list.append(Vertex(id, x, y))

from data_structures.graph_classes.linked_list.singly_linked_list import SinglyLinkedList

class Vertex:
    def __init__(self, id, x, y):
        self.id = id # The id (number of the vertex)
        self.x = x # The x coordinates of the vertex
        self.y = y # The y coordinates of the vertex
        self._edges = SinglyLinkedList() # A linked list that will store all the id's of the vertexes edges

    def add_edge(self, edge):
        self._edges.append(edge) # Append an edge to the singularly linked list

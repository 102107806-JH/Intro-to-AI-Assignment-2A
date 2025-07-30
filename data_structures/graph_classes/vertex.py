from data_structures.graph_classes.linked_list.singly_linked_list import SinglyLinkedList

class Vertex:
    def __init__(self, id, x, y):
        self.id = id # The id (number of the vertex)
        self.x = x # The x coordinates of the vertex
        self.y = y # The y coordinates of the vertex
        self._edges = SinglyLinkedList() # A linked list that will store all the id's of the vertexes edges

    def add_edge(self, edge):
        self._edges.append(edge) # Append an edge to the singularly linked list

    def extract_edges_as_list(self):
        current_node = self._edges.get_head()
        edges_list = []
        while current_node is not None:
            edges_list.append(current_node.get_data())
            current_node = current_node.get_next()
        return edges_list
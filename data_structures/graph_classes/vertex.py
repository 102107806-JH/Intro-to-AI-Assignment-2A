from data_structures.graph_classes.linked_list.singly_linked_list import SinglyLinkedList

class Vertex:
    def __init__(self, id, x, y):
        self._id = id  # The id (number of the vertex) #
        self._x = x  # The x coordinates of the vertex #
        self._y = y  # The y coordinates of the vertex #
        self._edges = SinglyLinkedList()  # A linked list that will store all the id's of the vertexes edges #

    def add_edge(self, edge):
        self._edges.append(edge)  # Append an edge to the singularly linked list #

    @property
    def edges(self):  # Getting the edges in list format #
        # The below code extracts the data from the linked list and places it in list
        current_node = self._edges.head  # Set the current node to the head of the linked list #
        edges_list = []  # List that will store the extracted data from the linked list #

        # Traverse entire linked list extracting all the data and placing it in the edges list
        while current_node is not None:
            edges_list.append(current_node.data)
            current_node = current_node.next

        return edges_list

    @property
    def id(self):
        return self._id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
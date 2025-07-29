from data_structures.graph_classes.adjacency_list_graph import AdjacencyListGraph

class TextFileDataExtractor:
    def __init__(self, file_name):
        text_data_file = open(file_name)
        self._file_contents = text_data_file.read()
        text_data_file.close()

    def get_adjacency_list_graph(self):

        adjacency_list_graph = AdjacencyListGraph() # Initialize the adjacency list graph
        adjacency_list_graph = self._insert_vertexes_into_adjacency_list(adjacency_list_graph) # Insert vertexes into adjacency list grap

        print("end")
        """
        edges_text_start = self._file_contents.find("Edges:")
        edges_text_end = edges_text_start + len("Edges:")

        origin_text_start = self._file_contents.find("Origin:")
        origin_text_end = origin_text_start + len("Origin:")

        destinations_text_start = self._file_contents.find("Destinations:")
        destinations_text_end = destinations_text_start + len("Destinations:")

        # Placing the data into separate strings
        edges_data = self._file_contents[edges_text_end: origin_text_start]
        origin_data = self._file_contents[origin_text_end: destinations_text_start]
        destinations_data = self._file_contents[destinations_text_end: -1]
        """


    def _insert_vertexes_into_adjacency_list(self, adjacency_list_graph):
        # Seperating edges text
        nodes_text_end = self._file_contents.find("Nodes:") + len("Nodes:")
        edges_text_start = self._file_contents.find("Edges:")
        nodes_data = self._file_contents[nodes_text_end: edges_text_start]

        nodes_data_string = nodes_data.replace(" ", "").replace("\n", "")# Removing out all spaces and newline chars
        data_buffer = ""
        for c in nodes_data_string:

            if c == ":":
                id = int(data_buffer)
                data_buffer = ""
                continue
            elif c == "(":
                continue
            elif c == ",":
                x = int(data_buffer)
                data_buffer = ""
                continue
            elif c == ")":
                y = int(data_buffer)
                data_buffer = ""
                adjacency_list_graph.insert_vertex(id, x, y)
                continue

            data_buffer += c

        return adjacency_list_graph

    def













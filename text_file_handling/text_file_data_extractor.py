from data_structures.graph_classes.adjacency_list_graph import AdjacencyListGraph

class TextFileDataExtractor:
    def __init__(self, file_name):
        text_data_file = open(file_name)
        self._file_contents = text_data_file.read()
        text_data_file.close()

    def extract_text_file_data(self):

        adjacency_list_graph = AdjacencyListGraph() # Initialize the adjacency list graph

        adjacency_list_graph = self._insert_vertexes_into_adjacency_list(adjacency_list_graph) # Insert vertexes into adjacency list grap

        adjacency_list_graph = self._insert_edges_into_adjacency_list(adjacency_list_graph)

        origin = self._extract_origin()

        destinations_list = self._extract_destinations()

        return ExtractedTextFileData(adjacency_list_graph, origin, destinations_list)

    def _insert_vertexes_into_adjacency_list(self, adjacency_list_graph):
        # Seperating edges text
        nodes_text_end = self._file_contents.find("Nodes:") + len("Nodes:")
        edges_text_start = self._file_contents.find("Edges:")
        nodes_data_string = self._file_contents[nodes_text_end: edges_text_start]
        nodes_data_string = nodes_data_string.replace(" ", "").replace("\n", "")# Removing out all spaces and newline chars

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

    def _insert_edges_into_adjacency_list(self, adjacency_list_graph):

        edges_text_end = self._file_contents.find("Edges:") + len("Edges:")
        origin_text_start = self._file_contents.find("Origin:")
        edges_data_string = self._file_contents[edges_text_end: origin_text_start]
        edges_data_string = edges_data_string.replace(" ", "").replace("\n", "")  # Removing out all spaces and newline chars

        edges_data_string = edges_data_string.replace("(", "", 1)
        edges_data_string += "("

        data_buffer = ""
        for c in edges_data_string:

            if c == "(":
                cost = int(data_buffer)
                adjacency_list_graph.insert_edge_into_vertex(origin_id, destination_id, cost)
                data_buffer = ""
                continue
            elif c == ",":
                origin_id = int(data_buffer)
                data_buffer = ""
                continue
            elif c == ")":
                destination_id = int(data_buffer)
                data_buffer = ""
                continue
            elif c == ":":
                continue

            data_buffer += c

        return adjacency_list_graph

    def _extract_origin(self):
        origin_text_end = self._file_contents.find("Origin:") + len("Origin:")
        destinations_text_start = self._file_contents.find("Destinations:")
        origin_data_string = self._file_contents[origin_text_end: destinations_text_start]
        origin_data_string = origin_data_string.replace(" ", "").replace("\n", "")  # Removing out all spaces and newline chars

        return int(origin_data_string)

    def _extract_destinations(self):
        destinations_text_end = self._file_contents.find("Destinations:") + len("Destinations:")
        destinations_data_string = self._file_contents[destinations_text_end: -1]
        destinations_data_string = destinations_data_string.replace(" ", "").replace("\n", "")  # Removing out all spaces and newline chars

        destinations_data_string += ";"
        data_buffer = ""
        destinations_list = []
        for c in destinations_data_string:

            if c == ";":
                destinations_list.append(int(data_buffer))
                data_buffer = ""
                continue
            data_buffer += c

        return destinations_list

class ExtractedTextFileData:
    def __init__(self, adjacency_list_graph, origin, destinations_list):
        self.adjacency_list_graph = adjacency_list_graph
        self.origin = origin
        self.destinations_list = destinations_list











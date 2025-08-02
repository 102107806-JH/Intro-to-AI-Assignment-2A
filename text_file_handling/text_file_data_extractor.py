from data_structures.graph_classes.adjacency_list_graph import AdjacencyListGraph


class TextFileDataExtractor:
    def __init__(self, file_name):
        text_data_file = open(file_name)  # Open the text file #
        self._file_contents = text_data_file.read()  # Read the text files contents #
        text_data_file.close()  # Close the text file #

    def extract_text_file_data(self):
        adjacency_list_graph = AdjacencyListGraph()  # Initialize the adjacency list graph with its constructor #

        adjacency_list_graph = self._insert_vertexes_into_adjacency_list(adjacency_list_graph)
        # Insert vertexes into adjacency list graph from text file #

        adjacency_list_graph = self._insert_edges_into_adjacency_list(adjacency_list_graph)
        # Insert vertex edges from text file #

        origin = self._extract_origin()  # Get the origin from text file #

        destinations_list = self._extract_destinations()  # Get the destinations from the text file #

        return ExtractedTextFileData(adjacency_list_graph, origin, destinations_list)
        # Return the data in a wrapper object #

    def _insert_vertexes_into_adjacency_list(self, adjacency_list_graph):

        nodes_text_end = self._file_contents.find("Nodes:") + len("Nodes:")  # Start index of nodes data #
        edges_text_start = self._file_contents.find("Edges:")  # End index of the nodes data
        nodes_data_string = self._file_contents[nodes_text_end: edges_text_start]  # Slice nodes data #
        nodes_data_string = nodes_data_string.replace(" ", "").replace("\n", "")
        # Removing out all spaces and newline chars #

        # Raise exception data string is empty means that no nodes were provided #
        if len(nodes_data_string) == 0:
            raise Exception("No nodes have been provided in the text file! Please provide nodes!")

        data_buffer = ""  # Stores the data in the following for loop #
        for c in nodes_data_string:  # Loop through all chars in the node string data

            if c == ":":  # Have extracted the id #
                id = int(data_buffer)
                data_buffer = ""  # Reset the buffer #
                continue  # Prevents char from being added to buffer (same with the rest of the continues) #
            elif c == "(":
                continue
            elif c == ",":  # Have extracted the x #
                x = int(data_buffer)
                data_buffer = ""
                continue
            elif c == ")":  # Have extracted the y #
                y = int(data_buffer)
                data_buffer = ""
                adjacency_list_graph.insert_vertex(id, x, y)
                continue

            data_buffer += c  # Add char to the data buffer #

        return adjacency_list_graph

    def _insert_edges_into_adjacency_list(self, adjacency_list_graph):

        edges_text_end = self._file_contents.find("Edges:") + len("Edges:")  # Start index of the edges' data #
        origin_text_start = self._file_contents.find("Origin:")  # End index of the edges' data #
        edges_data_string = self._file_contents[edges_text_end: origin_text_start]  # Slice nodes data #
        edges_data_string = edges_data_string.replace(" ", "").replace("\n", "")
        # Removing out all spaces and newline chars #

        # No edges provided further processing is unnecessary #
        if len(edges_data_string) == 0:
            return adjacency_list_graph

        # Below two lines format the string to make dealing with it easier #
        edges_data_string = edges_data_string.replace("(", "", 1)
        edges_data_string += "("

        data_buffer = ""  # Stores the data in the following for loop #
        for c in edges_data_string:

            if c == ",":  # Origin id has been found
                origin_id = int(data_buffer)
                data_buffer = ""  # Clear the data buffer #
                continue  # Ensure that char is not added to data buffer (All continues to do the same) #
            elif c == ")":
                destination_id = int(data_buffer)
                data_buffer = ""
                continue
            elif c == ":":
                continue
            elif c == "(":  # Cost has been extracted
                cost = float(data_buffer)
                adjacency_list_graph.insert_edge_into_vertex(origin_id, destination_id, cost)
                # Insert a new edges into the graph #
                data_buffer = ""
                continue

            data_buffer += c  # Add char to the data buffer #

        return adjacency_list_graph

    def _extract_origin(self):

        origin_text_end = self._file_contents.find("Origin:") + len("Origin:")  # Start index of the origin data #
        destinations_text_start = self._file_contents.find("Destinations:")  # End index of the origin data #
        origin_data_string = self._file_contents[origin_text_end: destinations_text_start]
        # Slice out the origin data #
        origin_data_string = origin_data_string.replace(" ", "").replace("\n", "")
        # Removing out all spaces and newline chars #

        # Raise exception data string is empty means that no origin was provided #
        if len(origin_data_string) == 0:
            raise Exception("No origin has been provided in the text file! Please provide origin!")

        return int(origin_data_string)  # No need for loop the origin data consists of one integer

    def _extract_destinations(self):

        destinations_text_end = self._file_contents.find("Destinations:") + len("Destinations:")
        # Start index of the destinations' data #
        destinations_data_string = self._file_contents[destinations_text_end: -1]
        # Slice out the destinations' data (no end index needs to be calculated because it goes up string end) #
        destinations_data_string = destinations_data_string.replace(" ", "").replace("\n", "")
        # Removing out all spaces and newline chars #

        # Raise exception data string is empty means that no origin was provided #
        if len(destinations_data_string) == 0:
            raise Exception("No destination(s) has been provided in the text file! Please provide a destination(s)!")

        destinations_data_string += ";"  # Formatting string to make it easier to deal with #

        data_buffer = ""  # Data buffer #
        destinations_list = []  # A list that will store all the destinations as integers #
        for c in destinations_data_string:

            if c == ";" and len(data_buffer) != 0:  # Have found a destination #
                destinations_list.append(int(data_buffer))  # Append the destination to the list #
                data_buffer = ""  # Reset the data buffer #
                continue  # Don't want the current char added to the data buffer #

            data_buffer += c  # Add char to the data buffer #

        return destinations_list


class ExtractedTextFileData:  # Helper object that acts as a struct was added in this file for sake of simplicity #
    def __init__(self, adjacency_list_graph, origin, destinations_list):
        self._adjacency_list_graph = adjacency_list_graph
        self._origin = origin
        self._destinations_list = destinations_list

    @property
    def adjacency_list_graph(self):
        return self._adjacency_list_graph

    @property
    def origin(self):
        return self._origin

    @property
    def destinations_list(self):
        return self._destinations_list
class GraphInitialization:
    def __init__(self, file_name):
        text_data_file = open(file_name)
        self._file_contents = text_data_file.read()
        text_data_file.close()

    def get_adjacency_list_graph(self):
        #self._file_contents = self._file_contents[6:-1]
        print(self._file_contents.find("Edges"))
        #print(self._file_contents)


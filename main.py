from text_file_handling.text_file_data_extractor import TextFileDataExtractor

text_file_extractor = TextFileDataExtractor(r"data/PathFinder-test.txt")
text_file_extractor.get_adjacency_list_graph()
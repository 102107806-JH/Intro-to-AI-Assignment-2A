from text_file_handling.text_file_data_extractor import TextFileDataExtractor

text_file_extractor = TextFileDataExtractor(r"data/PathFinder-test.txt")
data = text_file_extractor.extract_text_file_data()

print("END")
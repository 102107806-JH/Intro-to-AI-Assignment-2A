from text_file_handling.text_file_data_extractor import TextFileDataExtractor
from problem.problem import Problem

text_file_extractor = TextFileDataExtractor(r"data/PathFinder-test.txt")
extracted_text_file_data_object = text_file_extractor.extract_text_file_data()

problem = Problem(extracted_text_file_data_object)

actions = problem.actions(1)
print(problem.result(1, 3))
print(problem.action_cost(1, 3, 3))

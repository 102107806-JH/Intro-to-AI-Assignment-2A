import unittest
from search_algorithms.greedy_best_first_search import greed_best_first_search
from text_file_handling.text_file_data_extractor import TextFileDataExtractor
from textbook_abstractions.problem import Problem


class TestDFS(unittest.TestCase):

    def generate_problem(self, filename):
        text_file_extractor = TextFileDataExtractor(filename)
        extracted_text_file_data_object = text_file_extractor.extract_text_file_data()
        problem = Problem(extracted_text_file_data_object)
        return problem

    def get_solution_path_list(self, node):
        path = []
        current = node
        while current:
            path.append(current.state)
            current = current.parent
        path.reverse()
        return path

    def test_optimal_path_unreachable_goal(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/optimal_path_unreachable_goal.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1, 3 ,4, 6, 7, 9, 8]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #

        self.assertEqual(expected_path_list, actual_path_list)

    def test_unreachable_goal(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/unreachable_goal.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = []  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #

        self.assertEqual(expected_path_list, actual_path_list)

    def test_ascending_order_expansion_when_all_else_equal(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/test_ascending_order_expansion_when_all_else_equal.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1, 2, 4, 5, 7]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #

        self.assertEqual(expected_path_list, actual_path_list)

    def test_worse_greedy_path(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/worse_greedy_path.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1, 4, 3, 5, 8, 9, 10, 7, 6]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #

        self.assertEqual(expected_path_list, actual_path_list)


if __name__ == '__main__':
    unittest.main()
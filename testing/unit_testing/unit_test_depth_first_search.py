import unittest
from search_algorithms.depth_first_search import depth_first_search
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

    def test_assignment_example(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/assignment_example.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=2)

        expected_path_list = [2, 1, 3, 2, 1, 4]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #

        self.assertEqual(expected_path_list, actual_path_list)

    def test_unreachable_goal(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/unreachable_goal.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=2)

        expected_path_list = []  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #

        self.assertEqual(expected_path_list, actual_path_list)

    def test_goal_beyond_depth(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/goal_beyond_depth.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter() - 1, cycle_depth_limit=2)

        expected_path_list = []  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #

        self.assertEqual(expected_path_list, actual_path_list)



if __name__ == '__main__':
    unittest.main()
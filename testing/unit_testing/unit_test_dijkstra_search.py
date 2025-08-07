import unittest
from search_algorithms.dijkstra_search import dijkstra_search
from text_file_handling.text_file_data_extractor import TextFileDataExtractor
from textbook_abstractions.problem import Problem


class TestDijkstra(unittest.TestCase):

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

    def test_optimal_path_assignment_example(self):
        problem = self.generate_problem(r"unit_testing_data/assignment_example.txt")
        solution_node = dijkstra_search(problem)

        expected_path_list = [2, 1, 4]
        actual_path_list = self.get_solution_path_list(solution_node)

        self.assertEqual(expected_path_list, actual_path_list)
        self.assertEqual(10.0, solution_node.path_cost) # Verify the path cost

    def test_unreachable_goal(self):
        problem = self.generate_problem(r"unit_testing_data/unreachable_goal.txt")
        solution_node = dijkstra_search(problem)

        expected_path_list = []  # No solution expected
        actual_path_list = self.get_solution_path_list(solution_node) if solution_node else []

        self.assertEqual(expected_path_list, actual_path_list)

    def test_optimal_path_complex(self):
        problem = self.generate_problem(r"unit_testing_data/optimal_path_unreachable_goal.txt")
        solution_node = dijkstra_search(problem)

        expected_path_list = [1, 2, 8]
        actual_path_list = self.get_solution_path_list(solution_node)

        self.assertEqual(expected_path_list, actual_path_list)
        self.assertEqual(9.0, solution_node.path_cost) # Verify the path cost

    def test_tie_breaking_ascending_order(self):
        problem = self.generate_problem(
            r"unit_testing_data/ascending_order_expansion_when_all_else_equal.txt")
        solution_node = dijkstra_search(problem)

        expected_path_list = [1, 2, 4, 5, 7]
        actual_path_list = self.get_solution_path_list(solution_node)

        self.assertEqual(expected_path_list, actual_path_list)
        self.assertEqual(8.0, solution_node.path_cost) # Verify the path cost

    def test_dijkstra_optimal_cost_path(self):
        problem = self.generate_problem(r"unit_testing_data/dijkstra_optimal_cost_test.txt")
        solution_node = dijkstra_search(problem)

        expected_path_list = [1, 3, 4]
        actual_path_list = self.get_solution_path_list(solution_node)

        self.assertEqual(expected_path_list, actual_path_list)
        self.assertEqual(6.0, solution_node.path_cost) # Verify the path cost

if __name__ == '__main__':
    unittest.main()
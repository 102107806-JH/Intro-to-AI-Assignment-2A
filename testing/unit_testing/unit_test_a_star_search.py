import unittest
from search_algorithms.a_star_search import a_star_search
from text_file_handling.text_file_data_extractor import TextFileDataExtractor
from textbook_abstractions.problem import Problem


def generate_problem(filename):
    text_file_extractor = TextFileDataExtractor(filename)
    extracted_text_file_data_object = text_file_extractor.extract_text_file_data()
    problem = Problem(extracted_text_file_data_object)
    return problem


def get_solution_path_list(node):
    path = []
    current = node
    while current:
        path.append(current.state)
        current = current.parent
    path.reverse()
    return path


class TestAStar(unittest.TestCase):

    def test_optimal_path_assignment_example(self):
        problem = generate_problem(r"unit_testing_data/assignment_example.txt")
        solution_node = a_star_search(problem)

        # Expected path: 2 -> 1 -> 4 (cost 10)
        expected_path_list = [2, 1, 4]
        actual_path_list = get_solution_path_list(solution_node)

        self.assertEqual(expected_path_list, actual_path_list)
        self.assertEqual(10.0, solution_node.path_cost)  # Verify the path cost

    def test_unreachable_goal(self):
        problem = generate_problem(r"unit_testing_data/unreachable_goal.txt")
        solution_node = a_star_search(problem)

        expected_path_list = []  # No solution expected
        actual_path_list = get_solution_path_list(solution_node) if solution_node else []

        self.assertEqual(expected_path_list, actual_path_list)

    def test_ascending_order_expansion_when_all_else_equal(self):
        problem = generate_problem(
            r"unit_testing_data/ascending_order_expansion_when_all_else_equal.txt")
        solution_node = a_star_search(problem)

        expected_path_list = [1, 2, 4, 5, 7]
        actual_path_list = get_solution_path_list(solution_node)

        self.assertEqual(expected_path_list, actual_path_list)
        self.assertEqual(8.0, solution_node.path_cost)  # Verify the path cost

    def test_worse_greedy_path_optimality(self):
        problem = generate_problem(r"unit_testing_data/worse_greedy_path.txt")
        solution_node = a_star_search(problem)

        expected_path_list = [1, 2, 6]
        actual_path_list = get_solution_path_list(solution_node)

        self.assertEqual(expected_path_list, actual_path_list)
        self.assertEqual(10.0, solution_node.path_cost)  # Verify the path cost


def test_tie_breaking_rule(self):
    problem = generate_problem(r"unit_testing_data/tie_breaking_test.txt")
    solution_node = a_star_search(problem)

    expected_path_list = [1, 2, 4]
    actual_path_list = get_solution_path_list(solution_node)

    self.assertEqual(expected_path_list, actual_path_list)
    self.assertEqual(10.0, solution_node.path_cost)  # Verify the path cost


if __name__ == '__main__':
    unittest.main()
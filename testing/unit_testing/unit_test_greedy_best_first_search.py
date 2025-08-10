import unittest
from search_algorithms.greedy_best_first_search import greed_best_first_search
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


class TestDFS(unittest.TestCase):

    def test_optimal_path_unreachable_goal(self):
        # Problem generation and search execution
        problem = generate_problem(r"unit_testing_data/optimal_path_unreachable_goal.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1, 3, 4, 6, 7, 9, 8]  # Expected path list #
        actual_path_list = get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 13.73
        actual_path_cost = round(solution_node.path_cost, 2)
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_unreachable_goal(self):
        problem = generate_problem(r"unit_testing_data/unreachable_goal.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = []
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

    def test_ascending_order_expansion_when_all_else_equal(self):
        problem = generate_problem(
            r"unit_testing_data/ascending_order_expansion_when_all_else_equal.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1, 2, 4, 5, 7]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 8
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_worse_greedy_path(self):
        problem = generate_problem(r"unit_testing_data/worse_greedy_path.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1, 4, 3, 5, 8, 9, 10, 7, 6]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 40
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_gbfs_better_pop_later(self):
        problem = generate_problem(r"unit_testing_data/gbfs_better_pop_later.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [5, 6, 3, 1, 4]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 96
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_origin_is_goal(self):
        problem = generate_problem(r"unit_testing_data/origin_is_goal.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 0
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_multiple_goals_and_tie_brake(self):
        problem = generate_problem(r"unit_testing_data/multiple_goals.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [1, 2, 4]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 15
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_gbfs_better_pop_later_multiple_times(self):
        problem = generate_problem(
            r"unit_testing_data/gbfs_better_pop_whilst_node_still_on_stack.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [5, 6, 3, 1, 4, 11, 12, 9, 7, 10]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 194
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_gbfs_better_pop_whilst_node_still_on_stack(self):
        problem = generate_problem(r"unit_testing_data/gbfs_better_pop_whilst_node_still_on_stack.txt")
        solution_node = greed_best_first_search(problem)

        expected_path_list = [5, 6, 3, 1, 4, 11, 12, 9, 7, 10]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 194
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)


if __name__ == '__main__':
    unittest.main()
import unittest
from search_algorithms.weighted_A_star import weighted_A_star
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


class TestWeightedAStar(unittest.TestCase):

    def test_high_and_low_weight(self):
        # Problem generation and search execution
        problem = generate_problem(r"unit_testing_data/optimal_path_unreachable_goal.txt")
        solution_node_low_weight = weighted_A_star(problem, weight=2)
        solution_node_high_weight = weighted_A_star(problem, weight=10)

        expected_path_list_low_weight = [1, 2, 8]  # Expected path list for the low weight #
        expected_path_list_high_weight = [1, 3, 4, 6, 7, 9, 8]  # Expected path list for the high weight #
        actual_path_list_low_weight = get_solution_path_list(
            solution_node_low_weight)  # Resulting path list for low weight #
        actual_path_list_high_weight = get_solution_path_list(
            solution_node_high_weight)  # Resulting path list for high weight #
        self.assertEqual(expected_path_list_low_weight, actual_path_list_low_weight)
        self.assertEqual(expected_path_list_high_weight, actual_path_list_high_weight)

    def test_unreachable_goal(self):
        problem = generate_problem(r"unit_testing_data/unreachable_goal.txt")
        solution_node = weighted_A_star(problem, weight=2)

        expected_path_list = []
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

    def test_ascending_order_expansion_when_all_else_equal(self):
        problem = generate_problem(
            r"unit_testing_data/ascending_order_expansion_when_all_else_equal.txt")
        solution_node = weighted_A_star(problem, weight=2)

        expected_path_list = [1, 2, 4, 5, 7]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 8
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_worse_greedy_path(self):
        problem = generate_problem(r"unit_testing_data/worse_greedy_path.txt")
        solution_node = weighted_A_star(problem, weight=1)

        expected_path_list = [1, 2, 6]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 10
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_better_node_popped_later(self):
        problem = generate_problem(r"unit_testing_data/wastar_better_path_later_pop.txt")
        solution_node = weighted_A_star(problem, weight=20)

        expected_path_list = [1, 4, 2, 3]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 1090
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_better_node_popped_later_v2(self):
        problem = generate_problem(r"unit_testing_data/wastar_better_path_later_pop_v2.txt")
        solution_node = weighted_A_star(problem, weight=20)

        expected_path_list = [1, 6, 2, 3, 4, 5]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 1093
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_origin_is_goal(self):
        problem = generate_problem(r"unit_testing_data/origin_is_goal.txt")
        solution_node = weighted_A_star(problem, weight=20)

        expected_path_list = [1]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 0
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_wastar_better_path_multiple_times_one_after_pop_one_whilst_on_stack(self):
        problem = generate_problem(
            r"unit_testing_data/wastar_better_path_multiple_times_one_after_pop_one_whilst_on_stack.txt")
        solution_node = weighted_A_star(problem, weight=20)

        expected_path_list = [1, 4, 2, 3, 5, 8, 7]
        actual_path_list = get_solution_path_list(solution_node)
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 1250
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)


if __name__ == '__main__':
    unittest.main()
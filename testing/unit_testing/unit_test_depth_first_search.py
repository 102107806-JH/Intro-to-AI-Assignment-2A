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

        expected_path_cost = 24
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

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

    def test_ascending_order_expansion_when_all_else_equal(self):
        # Problem generation and search execution
        problem = self.generate_problem(
            r"unit_testing_data/ascending_order_expansion_when_all_else_equal.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=0)

        expected_path_list = [1, 2, 1, 2, 4, 5, 7]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 12
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_multiple_paths_between_nodes(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/multiple_paths_between_nodes.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=0)

        expected_path_list = [1, 2, 1, 2, 4, 5, 7]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 30
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_origin_is_goal(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/origin_is_goal.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=0)

        expected_path_list = [1]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 0
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_potentially_infinite_loop_no_solution(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/dfs_potentially_infinite_loop_no_solution.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=0)

        expected_path_list = []  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

    def test_no_cycles_when_cycle_depth_is_graph_diameter(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/dfs_no_cycles_when_cycle_depth_is_graph_diameter.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=problem.get_graph_diameter())

        expected_path_list = [1, 2, 4, 5, 7]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 8
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_multiple_goals_when_maximum_cycle_depth_check(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/multiple_goals.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=problem.get_graph_diameter())

        expected_path_list = [1, 2, 3, 4]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 22
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)

    def test_multiple_goals_when_minimum_cycle_depth_check(self):
        # Problem generation and search execution
        problem = self.generate_problem(r"unit_testing_data/multiple_goals.txt")
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=0)

        expected_path_list = [1, 2, 1, 2, 1, 2, 4]  # Expected path list #
        actual_path_list = self.get_solution_path_list(solution_node)  # Resulting path list #
        self.assertEqual(expected_path_list, actual_path_list)

        expected_path_cost = 35
        actual_path_cost = solution_node.path_cost
        self.assertEqual(expected_path_cost, actual_path_cost)



if __name__ == '__main__':
    unittest.main()
import sys
import os
from text_file_handling.text_file_data_extractor import TextFileDataExtractor
from textbook_abstractions.problem import Problem
from textbook_abstractions.node import Node
from search_algorithms.breadth_first_search import breadth_first_search
from search_algorithms.depth_first_search import depth_first_search
from search_algorithms.greedy_best_first_search import greed_best_first_search
from search_algorithms.weighted_A_star import weighted_A_star
from search_algorithms.a_star_search import a_star_search
from search_algorithms.dijkstra_search import dijkstra_search  # Import the new algorithm


def get_solution_path(node):
    """
    Reconstructs the path from the initial state to the given goal node.
    Returns a list of node states representing the path.
    """
    path = []
    current = node
    while current:
        path.append(str(current.state))
        current = current.parent
    return " ".join(path[::-1])


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <filename> <method>")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].lower()

    Node.reset_node_count()

    try:
        text_file_extractor = TextFileDataExtractor(filename)
        extracted_text_file_data_object = text_file_extractor.extract_text_file_data()
        problem = Problem(extracted_text_file_data_object)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file '{filename}': {e}")
        sys.exit(1)

    solution_node = None
    if method == "bfs":
        solution_node = breadth_first_search(problem)
    elif method == "dfs":
        solution_node = depth_first_search(problem, depth_limit=problem.get_graph_diameter(), cycle_depth_limit=2)
    elif method == "gbfs":
        solution_node = greed_best_first_search(problem)
    elif method == "wastar":
        solution_node = weighted_A_star(problem, weight=2)
    elif method == "astar":
        solution_node = a_star_search(problem)
    elif method == "dijkstra":
        solution_node = dijkstra_search(problem)
    else:
        print(f"Error: Unknown search method '{method}'. Supported methods: bfs, dfs, gbfs, wastar, astar, dijkstra")
        sys.exit(1)

    if solution_node:
        print(f"{filename.split('/')[-1]} {method}")
        print(f"{solution_node.state} {Node.get_node_count()}")
        print(get_solution_path(solution_node))
    else:
        print(f"{filename.split('/')[-1]} {method}")
        print("No solution found.")


if __name__ == "__main__":
    main()
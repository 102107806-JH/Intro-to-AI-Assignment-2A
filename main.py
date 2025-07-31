import sys
from text_file_handling.text_file_data_extractor import TextFileDataExtractor
from textbook_abstractions.problem import Problem
from textbook_abstractions.node import Node  # Import Node to access the static methods
from search_algorithms.breadth_first_search import breadth_first_search
from search_algorithms.depth_first_search import depth_first_search

def get_solution_path(node):
    """
    Reconstructs the path from the initial state to the given goal node.
    Returns a list of node states representing the path.
    """
    path = []
    current = node
    while current:
        path.append(str(current.state))  # Convert to string for output
        current = current.parent
    return " ".join(path[::-1])  # Reverse the list to get start to goal order and join


def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <filename> <method>")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].lower()  # Convert method to lowercase for case-insensitivity

    # Reset node count before starting the search for a clean count
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
        solution_node = depth_first_search(problem, expansion_depth_limit=1)
    else:
        print(f"Error: Unknown search method '{method}'. Supported methods: bfs")
        sys.exit(1)

    # Output results
    if solution_node:
        # filename method
        print(f"{filename.split('/')[-1]} {method}")  # Extract just the file name
        # goal number_of_nodes
        print(f"{solution_node.state} {Node.get_node_count()}")
        # path
        print(get_solution_path(solution_node))
    else:
        # If no solution is found, print a failure message
        # The prompt only specifies output for "when a goal can be reached".
        print(f"{filename.split('/')[-1]} {method}")
        print("No solution found.")


if __name__ == "__main__":
    main()
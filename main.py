from text_file_handling.text_file_data_extractor import TextFileDataExtractor
from textbook_abstractions.problem import Problem

text_file_extractor = TextFileDataExtractor(r"data/PathFinder-test.txt")  # Create object to extract the text file data #

extracted_text_file_data_object = text_file_extractor.extract_text_file_data()  # Extract the data from text file and store inside wrapper object #

problem = Problem(extracted_text_file_data_object)  # Transfer the extracted text file data object into a problem

# PROBLEM DEMONSTRATION (The graph loaded is the one from the task sheet)

state = 3
action = 5
new_state = 5

# Prints a list of actions available from the current node.
# The actions are expressed as integers. These are the number of the nodes that can be traversed to
print("Available actions from state " + str(state) + ":", problem.actions(state=state))

# Gives the integer of the node that will be traversed to after the action
# This just returns the action integer because the action states which node will be travelled to
print("Result state after performing action " + str(action) + " on state " + str(state) + ":", problem.result(state=state, action=action))

# Gives the cost of performing a given action on a state
print("Cost of moving from state " + str(state) + " to " + str(new_state) + ":", problem.action_cost(state=state, action=action, new_state=new_state))

# Returns a boolean indicating whether state is a goal state
print("Is the state a goal?:", problem.is_goal(state))
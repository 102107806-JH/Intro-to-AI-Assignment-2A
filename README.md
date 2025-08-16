Project Directory Structure:
`    <Project>
       | data/: Contains .txt files that define the graphs and problems used for testing and execution.
       | data_structures/: Holds custom data structures for each search algorithm.
       |-->     graph_classes/: Contains the adjacency_list.py and other files for the graph representation.
       |-->     queues/: Includes custom implementations for the fifo_queue.py, priority_queue.py, and stack_queue.py
       | search_algorithms/: Contains the implementation for each search algorithm.
       | testing/: Contains all unit and integration tests.
       |-->     unit_testing_data/: Stores the data files and corresponding .png visualizations for all unit tests.
       | text_file_handling/: Contains the text_file_data_extractor.py for parsing the problem text files.
       | textbook_abstractions/: Contains node.py and problem.py which are the abstractions used in the textbook.
       | old_files/: Contains the old files that were used for testing purposes and are not currently implemented in the 
         final solution, they may be disregarded or used as evidence of development.`


How to Run Unit Tests:
Please open the source code using your editor of choice, 
then you can either run each unit test individually or run all of them at once for a selected algorithm.
1. Open the project in your editor.
2. Select a unit test algorithm file from the unit testing folder.
3. Run the file using your editor's built-in unit testing framework.
4. The unit test will run and display the results.


How to Run the Program:
Please use the command line interface using Search.py. 
1. cd to the path that contains /Intro-to-AI-Assignment-2A
2. run python search.py data/PathFinder-test.txt bfs - returns the Breadth First Search
3. run python search.py data/PathFinder-test.txt dfs - returns the Depth First Search
4. run python search.py data/PathFinder-test.txt astar - returns the A* Search
5. run python search.py data/PathFinder-test.txt gbfs - returns the Greedy Best First Search
6. run python search.py data/PathFinder-test.txt dijkstra - returns the Dijkstra Search
Example: python search.py data/PathFinder-test.txt bfs


Terms & Conditions:
THIS SOFTWARE IS PROVIDED 'AS-IS', WITHOUT ANY EXPRESS OR IMPLIED WARRANTY. 
	  IN NO EVENT WILL THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING FROM THE 
	  USE OF THIS SOFTWARE.
  
      Permission is granted to anyone to use this software for any purpose, 
	  excluding commercial applications subject to the following restrictions:
  
		1. The origin of this software must not be misrepresented; you must not claim 
		   that you wrote the original software.
		2. This software is a freeware, it cannot be sold or rented.
		3. This notice may not be removed or altered from any distribution.
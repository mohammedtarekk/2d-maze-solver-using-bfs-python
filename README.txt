- A simple generic program that solves any 2D maze using Breadth-First-Search (BFS) algorithm. 

- The input consists of the rows of the 2D maze seperated by spaces.

   Sample input:
   S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.
   Where:
	  S --> The starting node
          . --> Available position (valid move)
          # --> Obstacle (not valid move)
	  E --> The goal node
	  
   Output:
   	  1. The full path that was visited during searching for the goal node.
	  2. The shortest path from the start node to the goal node.

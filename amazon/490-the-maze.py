"""
https://leetcode.com/problems/the-maze/

490. The Maze

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through the empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, 
it could choose the next direction.

Given the maze, the ball's start position and the destination, 
where start = [startrow, startcol] and destination = [destinationrow, destinationcol], 
return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).


Example 1:

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
start = [0,4], destination = [4,4]

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
start = [0,4], destination = [3,2]

Output: false
Explanation: There is no way for the ball to stop at the destination. 
Notice that you can pass through the destination but you cannot stop there.

Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], 
destination = [0,1]

Output: false
 

Constraints:

1 <= maze.length, maze[i].length <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= maze.length
0 <= startcol, destinationcol <= maze[i].length
Both the ball and the destination exist on an empty space, 
and they will not be at the same position initially.
The maze contains at least 2 empty spaces.

"""

from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()
        return self.dfs(start[0], start[1], destination, visited, maze)

    def dfs(self, x, y, dest, visited, maze):
        if [x, y] == dest:
            return True
        for dx, dy in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x1, y1 = x, y
            while 0 <= x1 + dx < len(maze) and 0 <= y1 + dy < len(maze[0]) and not maze[x1 + dx][y1 + dy]:
                x1, y1 = x1 + dx, y1 + dy
            if (x1, y1) not in visited:
                visited.add((x1, y1))
                if self.dfs(x1, y1, dest, visited, maze):
                    return True
        return False

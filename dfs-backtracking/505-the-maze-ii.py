"""
https://leetcode.com/problems/the-maze-ii/

505. The Maze II

There is a ball in a maze with empty spaces and walls. 
The ball can go through empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, 
it could choose the next direction.

Given the ball's start position, the destination and the maze, 
find the shortest distance for the ball to stop at the destination. 
The distance is defined by the number of empty spaces traveled by the ball from the start position 
(excluded) to the destination (included). 
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
You may assume that the borders of the maze are all walls. 
The start and destination coordinates are represented by row and column indexes.

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, 
and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), 
but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

"""

import collections
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], s: List[int], t: List[int]) -> int:
        if maze[s[0]][s[1]] == 1:
            return -1
        m, n = len(maze), len(maze[0])
        q = collections.deque()
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        q.append((s[0], s[1]))
        dist[s[0]][s[1]] = 0
        while q:
            p, r = q.popleft()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                roll = dist[p][r]
                x, y = p, r
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    roll += 1
                if roll < dist[x][y]:
                    dist[x][y] = roll
                    q.append((x, y))
        if dist[t[0]][t[1]] == float('inf'):
            return -1
        return dist[t[0]][t[1]]

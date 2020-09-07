"""
https://leetcode.com/problems/rotting-oranges/

994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.
 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_fresh = 0
        queue = []
        step = 1
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    n_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, step))  # x, y, n_steps
                    visited.add((i, j))
        if n_fresh == 0:
            return 0
        while queue:
            # for _ in range(len(queue)):
            x, y, step = queue.pop(0)
            for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x_new, y_new = x + delta_x, y + delta_y
                if self.valid(x_new, y_new, grid, visited):
                    n_fresh -= 1
                    if n_fresh == 0:
                        return step
                    visited.add((x_new, y_new))
                    queue.append((x_new, y_new, step + 1))
        return -1

    def valid(self, x, y, grid, visited):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in visited

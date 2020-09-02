"""
https://leetcode-cn.com/problems/number-of-enclaves/

1020. Number of Enclaves

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 
Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.


Solution

- 用dfs从四周边缘的陆地出发
- 将每次经过的陆地修改成水
- 最后计算矩阵里面陆地数。这些陆地将是我们从边缘无法到达的地方。

Time complexity: O (V + E) -> O(V)
"""

from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        copy_A = [row[:] for row in A]
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] and (i == 0 or j == 0 or i == n - 1 or j == m - 1):
                    self.dfs(copy_A, i, j)
        return sum(sum(row) for row in copy_A)

    def dfs(self, A, x, y):
        A[x][y] = 0
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x_new = x + dx
            y_new = y + dy
            if 0 <= x_new < len(A) and 0 <= y_new < len(A[0]) and A[x_new][y_new]:
                self.dfs(A, x_new, y_new)
        return

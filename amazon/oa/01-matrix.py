"""
https://leetcode.com/problems/01-matrix/

542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 
"""

from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return matrix
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] = self.bfs(matrix, i, j)
        return matrix

    def bfs(self, matrix, i, j):
        queue = [(i, j, 0)]
        while queue:
            i, j, d = queue.pop(0)
            if matrix[i][j] == 0:
                return d
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                    queue.append((i + x, j + y, d + 1))
        return

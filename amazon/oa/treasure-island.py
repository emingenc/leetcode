"""
https://leetcode.com/discuss/interview-question/347457

You have a map that marks the location of a treasure island. 
Some of the map area has jagged rocks and dangerous reefs. 
Other areas are safe to sail in. 
There are other explorers trying to find the treasure. 
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, 
left or right at a time. 
The treasure island is marked as X in a block of the matrix. 
X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. 
You must not enter dangerous blocks. 
You cannot leave the map area. Other areas O are safe to sail in. 
The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) 
The minimum route takes 5 steps.

"""

import collections


def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1  # impossible

    matrix = [row[:] for row in m]
    nrow, ncol = len(matrix), len(matrix[0])
    q = collections.deque([((0, 0), 0)])  # ((x, y), step)
    matrix[0][0] = "D"  # visited
    while q:
        (x, y), step = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x_new, y_new = x + dx, y + dy
            if 0 <= x_new < nrow and 0 <= y_new < ncol:
                if matrix[x_new][y_new] == "X":
                    return step + 1
                elif matrix[x_new][y_new] == "O":
                    matrix[x_new][y_new] = "D"
                    q.append(((x_new, y_new), step + 1))

    return -1

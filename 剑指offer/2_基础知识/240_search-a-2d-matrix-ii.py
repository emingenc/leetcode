"""
https://leetcode.com/problems/search-a-2d-matrix-ii/


240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中

思路：从左下角或者右上角开始比较

"""


class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows - 1, 0
        while row >= 0 and col <= cols - 1:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

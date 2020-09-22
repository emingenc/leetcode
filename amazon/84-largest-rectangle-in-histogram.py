"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10

"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res, i = 0, 0
        while i < len(heights):
            if not stack or (heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                k = stack.pop()
                res = max(res, heights[k] *
                          ((i - stack[-1] - 1) if stack else i))
        while stack:
            k = stack.pop()
            res = max(res, heights[k]*((i - stack[-1] - 1) if stack else i))
        return res

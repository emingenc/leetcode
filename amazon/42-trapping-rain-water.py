"""
https://leetcode.com/problems/trapping-rain-water/

42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Solution 

从左向右计算每一个位置之前的最高高度
从右向左计算每一个位置之后的最高高度
对于每一个位置的容积是左边最大高度和右边最大高度的最小值减去当前位置的高度
将所有位置容积相加就是总容积数

"""

from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left_max = [0] * n
        left_max[0] = heights[0]
        right_max = [0] * n
        right_max[n - 1] = heights[n - 1]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], heights[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], heights[i])
        ans = 0
        for i in range(1, n - 1):
            ans += min(left_max[i], right_max[i]) - heights[i]
        return ans

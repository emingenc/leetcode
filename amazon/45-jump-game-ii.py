"""
https://leetcode.com/problems/jump-game-ii/

45. Jump Game II

Given an array of non-negative integers, 
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

"""

from typing import List
import collections


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        visited = set([0])
        q = collections.deque()
        q.append((0, 0))  # position, step
        while q:
            cur, step = q.popleft()
            if cur + nums[cur] >= n-1:
                return step + 1
            for i in range(nums[cur], 0, -1):
                if cur + i not in visited:
                    q.append((cur + i, step + 1))
                    visited.add(cur + i)
        return -1

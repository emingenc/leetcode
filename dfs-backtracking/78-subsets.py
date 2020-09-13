"""
https://leetcode.com/problems/subsets/

78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


Time complexity: O(N * 2^N) to generate all subsets and then copy them into output list.

Space complexity: O(N * 2^N). 
This is exactly the number of solutions for subsets multiplied by the number NN of elements 
to keep for each subset.

For a given number, it could be present or absent (i.e. binary choice) in a subset solution. 
As as result, for N numbers, we would have in total 2^N choices (solutions).

"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs([], nums, res)
        return res

    def dfs(self, comb, nums, res):
        res.append(comb)
        for i in range(len(nums)):
            self.dfs(comb+[nums[i]], nums[i+1:], res)

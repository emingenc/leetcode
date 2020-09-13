"""
https://leetcode.com/problems/permutations/

46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self._permute([], nums, res, len(nums))
        return res

    def _permute(self, comb, nums, res, n):
        if len(comb) == n:
            res.append(comb)
            return
        for i in range(len(nums)):
            self._permute(comb + [nums[i]], nums[:i] + nums[i+1:], res, n)
        return

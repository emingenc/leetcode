"""
https://leetcode.com/problems/permutations-ii/

47. Permutations II

Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self._permute([], nums, res, len(nums))
        return res

    def _permute(self, comb, nums, res, n):
        if len(comb) == n:
            res.append(comb)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self._permute(comb + [nums[i]], nums[:i] + nums[i+1:], res, n)
        return

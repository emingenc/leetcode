"""
https://leetcode.com/problems/combinations/

77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n

"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i+1 for i in range(n)]
        self._combine([], k, res, nums)
        return res

    def _combine(self, comb, k, res, nums):
        if len(comb) == k:
            res.append(comb)
            return
        for i in range(len(nums)):
            self._combine(comb+[nums[i]], k, res, nums[i+1:])
        return

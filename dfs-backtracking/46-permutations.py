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

Time complexity:
Time complexity : \mathcal{O}(\sum_{k = 1}^{N}{P(N, k)})
where P(N, k) = \frac{N!}{(N - k)!} = N (N - 1) ... (N - k + 1)
is so-called k-permutations_of_n, or partial permutation.


Space complexity : O(N!) since one has to keep N! solutions.

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

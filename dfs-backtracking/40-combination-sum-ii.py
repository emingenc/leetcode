"""
https://leetcode.com/problems/combination-sum-ii/

40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.dfs(sorted(candidates), target, [], results)
        return results

    def dfs(self, candidates, target, comb, results):
        if sum(comb) == target:
            results.append(comb)
        for i, num in enumerate(candidates):
            if sum(comb) + num > target:
                return
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates[i+1:], target, comb+[num], results)
        return

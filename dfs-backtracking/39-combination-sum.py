"""
https://leetcode.com/problems/combination-sum/

39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500

"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.dfs([], sorted(candidates), target, results)
        return results

    def dfs(self, comb, candidates, target, results):
        if sum(comb) == target:
            results.append(comb)
            return
        for i, num in enumerate(candidates):
            if comb and sum(comb) + num > target:
                return
            self.dfs(comb+[num], candidates[i:], target, results)
        return

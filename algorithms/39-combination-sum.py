# https://leetcode.com/problems/combination-sum/description/

"""
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

"""

# Fork from https://shenjie1993.gitbooks.io/leetcode-python/039%20Combination%20Sum.html

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combination(candidates, target, [], result)
        return result

    def combination(self, candidates, target, current, result):
        s = sum(current) if current else 0
        if s > target:
            return
        elif s == target:
            result.append(current)
            return
        else:
            for i, v in enumerate(candidates):
                self.combination(candidates[i:], target, current + [v], result)


if __name__ == "__main__":
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
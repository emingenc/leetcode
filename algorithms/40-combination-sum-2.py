# https://leetcode.com/problems/combination-sum-ii/description/

"""
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

# Fork from https://shenjie1993.gitbooks.io/leetcode-python/040%20Combination%20Sum%20II.html

class Solution(object):
    def combinationSum2(self, candidates, target):
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
            i = 0
            while i < len(candidates):
                self.combination(candidates[i + 1:], target, current + [candidates[i]], result)
                # ignore repeating elements
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1


if __name__ == "__main__":
    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
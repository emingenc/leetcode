"""
https://leetcode.com/problems/combination-sum-iii/

216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        nums = [i+1 for i in range(9)]
        self.dfs(nums, [], k, n, results)
        return results

    def dfs(self, nums, comb, k, n, results):
        if len(comb) == k and sum(comb) == n:
            results.append(comb)
            return
        for i in range(len(nums)):
            if sum(comb) + nums[i] > n or len(comb) > k:
                return
            self.dfs(nums[i+1:], comb+[nums[i]], k, n, results)
        return

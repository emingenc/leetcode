"""
https://leetcode.com/problems/combination-sum-iv/

377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = self.dfs(nums, target, 0, {})
        return count

    def dfs(self, nums, target, cur_sum, num_map):
        if cur_sum > target:
            return 0
        if cur_sum == target:
            return 1
        if cur_sum in num_map:
            return num_map[cur_sum]
        count = 0
        for num in nums:
            count += self.dfs(nums, target, cur_sum+num, num_map)
        num_map[cur_sum] = count
        return count


class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]

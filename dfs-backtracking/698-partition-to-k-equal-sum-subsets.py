"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

698. Partition to K Equal Sum Subsets

Given an array of integers nums and a positive integer k, 
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.


Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0 or max(nums) > sum(nums) / k:
            return False
        target = sum(nums) // k
        targets = [target] * k
        nums.sort(reverse=True)
        return self.dfs(nums, targets, 0, k)

    def dfs(self, nums, targets, cur_index, k):
        if cur_index == len(nums):
            return True
        num = nums[cur_index]
        for i in range(k):
            if targets[i] >= num:
                targets[i] -= num
                if self.dfs(nums, targets, cur_index + 1, k):
                    return True
                targets[i] += num
        return False

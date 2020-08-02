"""
Find Pair With Given Sum

https://leetcode.com/discuss/interview-question/356960

Given a list of positive integers nums and an int target,
return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
Solution
Related problems:

https://leetcode.com/problems/two-sum

"""


def givenSum(nums, target):
    dict_num = {}
    res = [-1, -1]
    max_num = float('-inf')
    for i, num in enumerate(nums):
        if num in dict_num:
            if num > max_num or nums[dict_num[num]] > max_num:
                res[0] = dict_num[num]
                res[1] = i
                max_num = max(num, nums[dict_num[num]])
        dict_num[target - num] = i
    return res


if __name__ == "__main__":
    for args in (
        (
            [1, 10, 25, 35, 60],
            90,
        ),
        (
            [20, 50, 40, 25, 30, 10],
            90,
        ),
        (
            [50, 20, 10, 40, 25, 30],
            90,
        ),
        (
            [1, 2],
            90,
        ),
    ):
        print(*args)
        print(givenSum(args[0], args[1] - 30))

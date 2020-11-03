"""
面试题41 和为s的两个数字VS和为s的连续正数序列

和为s的两个数字
要求：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s

思路: 设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加

"""


def sum_to_s(nums, s):
    head, end = 0, len(nums) - 1
    while head < end:
        if nums[head] + nums[end] == s:
            return [nums[head], nums[end]]
        elif nums[head] + nums[end] > s:
            end -= 1
        else:
            head += 1
    return None

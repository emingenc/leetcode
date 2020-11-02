"""
面试题29 数组中出现次数超过一半的数字
思路: 使用hash，key是数字，value是出现的次数

注意: 列表的len方法的时间复杂度是O(1)

"""


def get_more_than_half_num(nums):
    dict_num = {}
    n = len(nums)
    for num in nums:
        dict_num[num] = dict_num[num] + 1 if num in dict_num[num] else 1
        if dict_num[num] > n / 2:
            return num
    return 0

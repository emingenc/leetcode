"""
面试题44 扑克牌的顺子

要求：从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值

思路: 使用排序

"""


class Solution:
    def IsContinuous(self, numbers):
        #data = [random.choice(nums) for _ in range(k)]
        if not numbers:
            return False
        numbers.sort()
        zeros = numbers.count(0)
        gaps = 0
        small = zeros
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            gaps += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return gaps <= zeros

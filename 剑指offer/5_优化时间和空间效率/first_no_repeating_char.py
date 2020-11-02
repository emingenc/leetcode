"""
面试题35 第一个只出现一次的字符

要求：求字符串中第一个只出现一次的字符

"""

from collections import Counter


class Solution:

    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        counter = Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1

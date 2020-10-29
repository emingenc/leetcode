"""
https://leetcode.com/problems/add-strings/

415. Add Strings

Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""

DICT_STR_2_INT = {"1": 1, "2": 2, "3": 3, "4": 4,
                  "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        return str(self.str_to_int(num1) + self.str_to_int(num2))

    def str_to_int(self, num):
        res = 0
        k = 1
        for i in range(len(num)-1, -1, -1):
            res += DICT_STR_2_INT[num[i]]*k
            k *= 10
        return res

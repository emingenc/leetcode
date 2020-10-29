"""
https://leetcode.com/problems/add-binary/

67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

Solution

将两个字符串长度拉平，用零补充
分别放入两个栈
循环两个栈，每次取出一个和carry相加%2放到输出，如果和大于等于2, carry=1
循环结束如果carry是1，将1加到输出

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        if len_a < len_b:
            a = '0' * (len_b - len_a) + a
        else:
            b = '0' * (len_a - len_b) + b
        stack_a, stack_b = list(a), list(b)
        output = ''
        carry = 0
        while stack_a and stack_b:
            cur_sum = int(stack_a.pop()) + int(stack_b.pop()) + carry
            if cur_sum >= 2:
                cur_sum = cur_sum % 2
                carry = 1
            else:
                carry = 0
            output = str(cur_sum) + output
        if carry == 1:
            output = '1' + output
        return output

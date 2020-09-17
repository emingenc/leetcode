"""
https://leetcode.com/problems/palindrome-permutation/

266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true


Solution

回文串中，左右必须对称，因此出现次数为奇数的字符最多只有一个。
使用一个字典，保存每个字符出现的次数。如果出现次数为奇数个的字符<=1，那么可以构成回文串。

"""


import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        return len(list(filter(lambda x: x[1] % 2 != 0, counter.items()))) <= 1

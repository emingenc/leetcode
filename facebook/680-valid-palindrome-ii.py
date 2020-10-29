"""
https://leetcode.com/problems/valid-palindrome-ii/

680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True

Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. 
The maximum length of the string is 50000.


"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(x): return x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1: right + 1]) or isPalindrome(s[left: right])
        return True

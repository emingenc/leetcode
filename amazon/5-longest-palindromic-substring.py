"""
https://leetcode.com/problems/longest-palindromic-substring/

5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        ans = ''
        for i in range(N):
            for j in range(i + 1, N + 1):
                if j - i > len(ans) and self.isPalindrome(s[i:j]):
                    ans = s[i:j]
        return ans

    def isPalindrome(self, s):
        return s == s[::-1]

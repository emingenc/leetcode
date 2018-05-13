# https://leetcode.com/problems/longest-palindromic-substring/description/

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s):
        longest = ""

        for i, _ in enumerate(s):
            candidate = self.get_palindrome(s, start = i, end = i)

            if len(candidate) > len(longest):
                longest = candidate

        return longest

    @staticmethod
    def get_palindrome(s, start, end):
        while end + 1 < len(s) and s[end+1] == s[start]:
            end += 1

        while start > 0 and end + 1 < len(s) and s[start - 1] == s[end + 1]:
            start -= 1
            end += 1

        return s[start:end + 1]
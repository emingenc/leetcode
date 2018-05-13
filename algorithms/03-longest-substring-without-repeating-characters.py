# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/#

# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        max_len = 0
        sub_str = ''
        for str in s:
            if str not in sub_str:
                sub_str += str
                if len(sub_str) > max_len:
                    max_len = len(sub_str)
            else:
                sub_str = sub_str[sub_str.index(str)+1:] + str
        return max_len

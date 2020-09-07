"""
https://leetcode.com/problems/word-break/

139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self._canSplit(s, wordDict, memo)

    def _canSplit(self, word, wordDict, memo):
        if word in wordDict:
            return True
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            if self._canSplit(word[:i], wordDict, memo) and self._canSplit(word[i:], wordDict, memo):
                memo[word] = True
                return True
        memo[word] = False
        return False

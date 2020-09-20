"""
https://leetcode.com/problems/concatenated-words/

472. Concatenated Words

Given a list of words (without duplicates), please write a program that 
returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of 
at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.


Similar to leetcode 139. Word Break
        Time complexity: O(N^2)
        Space complexity: O(N)

"""

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Similar to leetcode 139. Word Break
        Time complexity: O(N^2)
        Space complexity: O(N)
        """
        res = []
        words = set(words)
        for word in words:
            if self.dfs(word, 0, words):
                res.append(word)
        return res

    def dfs(self, word, n_words, words):
        if not word and n_words >= 2:
            return True
        for i in range(len(word)):
            if word[:i + 1] in words and self.dfs(word[i + 1:], n_words + 1, words):
                return True
        return False

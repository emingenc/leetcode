"""
https://leetcode.com/problems/word-ladder-ii/

126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, 
such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if not endWord in wordSet:
            return []

        def edges(word):
            arr = list(word)
            for i in range(len(arr)):
                c = arr[i]
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    arr[i] = char
                    newWord = ''.join(arr)
                    if newWord in wordSet and not newWord in marked:
                        yield newWord
                arr[i] = c
        res = []
        marked = set()
        queue = [[beginWord]]
        while queue:
            temp = []
            found = False
            for words in queue:
                marked.add(words[-1])
            for words in queue:
                for w in edges(words[-1]):
                    v = words + [w]
                    if w == endWord:
                        res.append(v)
                        found = True
                    temp.append(v)
            if found:
                break
            queue = temp
        return res

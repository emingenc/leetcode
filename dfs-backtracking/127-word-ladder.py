"""
https://leetcode.com/problems/word-ladder/

127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


Solution 

宽度优先搜索
从左到右每次替换一个字符
每次从queue里pop出一个词并判断是否等于endWord
如果新词在字典里将新词加入queue从字典中取出新词


"""

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        queue = [(beginWord, 1)]
        seen = set()
        seen.add(beginWord)
        while queue:
            for _ in range(len(queue)):
                word, level = queue.pop(0)
                if word == endWord:
                    return level
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordset and newWord != word and newWord not in seen:
                            queue.append((newWord, level + 1))
                            # wordset.remove(newWord)
                            seen.add(newWord)
        return 0

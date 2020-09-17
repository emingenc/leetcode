"""
https://leetcode.com/problems/word-ladder-ii/

126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:

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

从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。 然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。

https://www.jiuzhang.com/solution/word-ladder-ii/#tag-lang-python


"""

from typing import List
import collections


class Solution:
    def findLadders(self, start: str, end: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or (start not in wordList and end not in wordList) or start == end:
            return []
        wordSet = set(wordList)
        wordSet.add(start)
        wordSet.add(end)
        distance = {}
        self.bfs(end, distance, wordSet)
        results = []
        self.dfs(start, end, distance, wordSet, [start], results)
        return results

    def get_next_words(self, word, wordSet):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in wordSet:
                    words.append(next_word)
        return words

    def bfs(self, start, distance, wordSet):
        distance[start] = 0
        queue = collections.deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, wordSet):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def dfs(self, curt, target, distance, wordSet, path, results):
        if curt == target:
            results.append(list(path))
            return
        for word in self.get_next_words(curt, wordSet):
            if distance[word] != distance[curt] - 1:
                continue
            # path.append(word)
            self.dfs(word, target, distance, wordSet, path + [word], results)
            # path.pop()
        return

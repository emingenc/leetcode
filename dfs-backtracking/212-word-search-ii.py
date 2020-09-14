"""
https://leetcode.com/problems/word-search-ii/

212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.


Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

"""

import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isWord


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        visited = set()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res, visited)
        return res

    def dfs(self, board, node, x, y, path, res, visited):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if not(0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited):
            return
        if board[x][y] not in node.children:
            return
        node = node.children[board[x][y]]
        visited.add((x, y))
        for delta_x, delta_y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            self.dfs(board, node, x + delta_x, y + delta_y,
                     path + board[x][y], res, visited)
        visited.remove((x, y))
        return

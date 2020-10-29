"""
https://leetcode.com/problems/alien-dictionary/

269. Alien Dictionary

There is a new alien language which uses the latin alphabet. 
However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

"""

from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""

        # a. Initialize the graph
        graph, indegree = {}, {}
        for word in words:
            for char in word:
                indegree[char] = 0
                graph[char] = []

        # b. Build the graph
        for i in range(0, len(words) - 1):
            # find ordering of characters from adjacent words
            cur_word, next_word = words[i], words[i+1]
            for j in range(0, min(len(cur_word), len(next_word))):
                parent, child = cur_word[j], next_word[j]
                if parent != child:
                    indegree[child] += 1
                    graph[parent].append(child)
                    break
                    # only the first different character between the two words will help

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = [node for node in indegree if indegree[node] == 0]

        # d. For each source, add it to the sortedOrder and subtract one from all of its
        # if a child's in-degree becomes zero, add it to the sources queue
        orders = []
        while sources:
            source = sources.pop(0)
            orders.append(source)
            for child in graph[source]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)

        # if sortedOrder doesn't contain all characters, there is a cyclic dependency bet
        # will not be able to find the correct ordering of the characters
        if len(orders) != len(indegree):
            return ""

        return ''.join(orders)

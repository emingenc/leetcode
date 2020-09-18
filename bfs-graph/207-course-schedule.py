"""
https://leetcode.com/problems/course-schedule/

207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

"""

import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)

        for cur, prev in prerequisites:
            graph[prev].append(cur)
            indegrees[cur] += 1

        sources = [cours for cours in range(
            numCourses) if not indegrees[cours]]
        order = set()

        while sources:
            # for _ in range(len(sources)):
            cours = sources.pop(0)
            order.add(cours)
            for child in graph[cours]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    sources.append(child)

        return len(order) == numCourses

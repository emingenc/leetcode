"""
https://leetcode.com/problems/accounts-merge/

721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, 
where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. 
Two accounts definitely belong to the same person if there is some email 
that is common to both accounts. 
Note that even if two accounts have the same name, they may belong to different people 
as people could have the same name. 
A person can have any number of accounts initially, 
but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: 
the first element of each account is the name, 
and the rest of the elements are emails in sorted order. 
The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

Explanation: 
The first and third John's are the same person 
as they have the common email "johnsmith@mail.com".

The second John and Mary are different people as 
none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer 
[['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] 
would still be accepted.

Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].

"""

import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = {}  #
        graph = collections.defaultdict(list)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[email].append(acc[1])
                graph[acc[1]].append(email)
                emails[email] = name
        visited = set()
        ans = []
        for email in emails:
            if email in visited:
                continue
            cur_group = []
            self.dfs(email, cur_group, visited, graph)
            ans.append([emails[email]] + sorted(cur_group))
        return ans

    def dfs(self, email, cur_group, visited, graph):
        if email in visited:
            return
        visited.add(email)
        cur_group.append(email)
        for neighbor in graph[email]:
            self.dfs(neighbor, cur_group, visited, graph)
        return

"""
https://leetcode.com/problems/clone-graph/

133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val = 1, the second node with val = 2, and so on. 
The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.


Constraints:

1 <= Node.val <= 100
Node.val is unique for each node.
Number of Nodes will not exceed 100.
There is no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

"""


class Node:
    # Definition for a Node.
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        que = [node]
        node_copy = Node(node.val, [])
        dict_node = {}
        dict_node[node] = node_copy
        while que:
            node = que.pop(0)
            if not node:
                continue
            for neighbor in node.neighbors:
                if neighbor not in dict_node:
                    dict_node[neighbor] = Node(neighbor.val, [])
                    que.append(neighbor)
                dict_node[node].neighbors.append(dict_node[neighbor])
        return node_copy

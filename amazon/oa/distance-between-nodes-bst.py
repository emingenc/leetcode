"""
Distance Between Nodes in BST

https://leetcode.com/discuss/interview-question/376375/


Given a list of unique integers nums, construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two nodes node1 and node2. Distance is the number of edges between two nodes. If any of the given nodes does not appear in the BST, return -1.

Example 1:

Input: nums = [2, 1, 3], node1 = 1, node2 = 3

Output: 2

Explanation:
     2
   /   \
  1     3
  

Time complexity: O(n * h), where n is the number of nodes and h is the height of the tree. In the worst case tree is not balanced (elements are already in sorted order) and complexity will be O(n^2).

Space complexity: O(n).


Related problems:

https://leetcode.com/problems/insert-into-a-binary-search-tree/

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


"""

# https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/#:~:text=The%20distance%20between%20two%20nodes%20can%20be%20obtained%20in%20terms,root%20of%20given%20Binary%20Tree.

"""
The distance between two nodes can be obtained in terms of lowest common ancestor. Following is the formula. 
 

Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) 
'n1' and 'n2' are the two given keys
'root' is root of given Binary Tree.
'lca' is lowest common ancestor of n1 and n2
Dist(n1, n2) is the distance between n1 and n2.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def pathToNode(root, path, k):

    # base case handling
    if root is None:
        return False

     # append the node value in path
    path.append(root.data)

    # See if the k is same as root's data
    if root.data == k:
        return True

    # Check if k is found in left or right
    # sub-tree
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right != None and pathToNode(root.right, path, k))):
        return True

    # If not present in subtree rooted with root,
    # remove root from path and return False
    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        # store path corresponding to node: data1
        path1 = []
        pathToNode(root, path1, data1)

        # store path corresponding to node: data2
        path2 = []
        pathToNode(root, path2, data2)

        # iterate through the paths to find the
        # common path length
        i = 0
        while i < len(path1) and i < len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i+1

        # get the path length by deducting the
        # intersecting path length (or till LCA)
        return (len(path1)+len(path2)-2*i)
    else:
        return 0


# Driver Code to test above functions
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)

dist = distance(root, 4, 5)
print("Distance between node {} & {}: {}".format(4, 5, dist))

dist = distance(root, 4, 6)
print("Distance between node {} & {}: {}".format(4, 6, dist))

dist = distance(root, 3, 4)
print("Distance between node {} & {}: {}".format(3, 4, dist))

dist = distance(root, 2, 4)
print("Distance between node {} & {}: {}".format(2, 4, dist))

dist = distance(root, 8, 5)
print("Distance between node {} & {}: {}".format(8, 5, dist))

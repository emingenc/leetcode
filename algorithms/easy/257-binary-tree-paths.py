# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        self.dfs(root, "", self.paths)
        return self.paths

    def dfs(self, node: TreeNode, path, paths):
        if node is None:
            return

        path += str(node.val)

        if node.left is None and node.right is None:
            paths.append(path)
            return

        if node.left is not None:
            self.dfs(node.left, path+'->', paths)

        if node.right is not None:
            self.dfs(node.right, path+'->', paths)

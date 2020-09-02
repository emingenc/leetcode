"""
https://leetcode-cn.com/problems/complete-binary-tree-inserter/


"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.tree = []
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                self.tree.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def insert(self, v: int) -> int:
        parent = self.tree[(len(self.tree) - 1) // 2]
        node = TreeNode(v)
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
        self.tree.append(node)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

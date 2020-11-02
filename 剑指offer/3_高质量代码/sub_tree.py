"""
面试题18 树的子结构
要求：判断一棵二叉树是不是另一个的子结构

思路：使用递归

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sub_tree(tree1, tree2):
    if (not tree1 and not tree2):
        return True
    if not tree1 or not tree2:
        return False
    if tree1.val == tree2.val:
        return sub_tree(tree1.left, tree2.left) and sub_tree(tree1.right, tree2.right)
    return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)

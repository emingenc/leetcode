"""
面试题39 二叉树的深度
思路: 分别递归的求左右子树的深度


"""


def get_depth(tree):
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return 1
    return 1 + max(get_depth(tree.left), get_depth(tree.right))

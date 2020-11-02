"""
面试题19 二叉树的镜像
思路一：可以按层次遍历，每一层从右到左

思路二：使用递归

"""

import collections


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def mirror_bfs(root):
    res = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node)
            queue.append(node.right)
            queue.append(node.left)
    return res


def mirror2(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    mirror2(root.left)
    mirror2(root.right)
    return


def levelOrder(root):
    if not root:
        return []
    output = []
    queue = [root]
    while queue:
        n = len(queue)
        cur_vals = []
        for _ in range(n):
            node = queue.pop(0)
            cur_vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(cur_vals)
    return output

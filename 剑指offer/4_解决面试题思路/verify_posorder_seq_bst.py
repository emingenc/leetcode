"""
面试题24 二叉搜索树的后序遍历序列
要求：判断给定的整数数组是不是二叉搜索树的后序遍历序列

整数数组中不包含重复值

整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树

题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

https://blog.csdn.net/fuxuemingzhu/article/details/79621107

解题方法
我们都知道BST的中序遍历是有序的，后序遍历时，最后的节点是根节点。
那么可以先找根节点，然后利用根节点的值，把数组分成两部分，前部分都比根节点小是左子树，后部分都比根节点大是右子树。
然后再分别遍历左右子树即可。
我做这个题的时候利用从左遍历找到第一个比根节点的大的位置划分左右节点，这样保证了左边部分都比根节点小，
不能保证右边部分都比根节点大，所以对右边的部分进行了验证。
另外题目中有个坑，题目认为，空树不是BST……所以新定义了函数进行递归，否则会更简单点。

"""


class Solution:
    def VerifySquenceOfBST(self, nums):
        if not nums:
            return False
        return self.verifyBST(nums)

    def verifyBST(self, nums):
        if not nums:
            return True
        root = nums.pop()
        index = self.findIndex(nums, root)
        if self.verifyRight(nums[index:], root):
            left = nums[:index]
            right = nums[index:]
            return self.verifyBST(left) and self.verifyBST(right)
        return False

    def verifyRight(self, nums, target):
        if not nums:
            return True
        return min(nums) > target

    def findIndex(self, nums, target):
        for i, num in enumerate(nums):
            if num > target:
                return i
        return len(nums)

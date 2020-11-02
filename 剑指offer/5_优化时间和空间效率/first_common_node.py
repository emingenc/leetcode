"""
面试题37 两个链表的第一个公共结点

思路: 先获取到两个链表的长度，然后长的链表先走多的几步，之后一起遍历

是从后往前找第一个不公共的节点

"""


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        pre = None
        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            pre = stack1.pop()
            stack2.pop()
        return pre

"""
https://github.com/JushuangQiao/Python-Offer/tree/master/fourth/fourth

面试题26 复杂链表的复制
要求：链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点

分为三步完成：

一:复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2

二:为每个新结点设置other指针

三:把复制后的结点链表拆开

题目描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

解题方法
这个题是分而治之的做法，很好玩。思想是在原来的链表每个节点后面都复制了一个同样的节点，再修改其指针，
最后把偶数节点都抽出来，作为新的复杂链表。

"""


class Node:
    def __init__(self, next=None, random=None):
        self.next = next
        self.random = next


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        dic = {}
        prior = Node(0)
        temp_1 = prior
        temp_2 = head
        while head:  # 构建next部分
            node = Node(head.val)
            dic[head] = node
            prior.next = node
            prior = node
            head = head.next

        prior.next = None
        temp_1 = temp_1.next
        result = temp_1
        head = temp_2
        while head:  # 构建random部分
            if not head.random:
                dic[head].random = None
            else:
                dic[head].random = dic[head.random]
            head = head.next

        return temp_1

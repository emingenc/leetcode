"""
面试题17 合并两个排序的链表
要求：合并两个排序的链表

思路：使用递归

"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_link_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val <= head2.val:
        head = head1
        head.next = merge_link_lists(head1.next, head2)
    else:
        head = head2
        head.next = merge_link_lists(head1, head2.next)
    return head

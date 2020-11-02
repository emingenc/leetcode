"""
面试题16 反转链表
要求：反转链表

思路：需要考虑空链表，只有一个结点的链表

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_linklist(head):
    if not head or not head.next:
        return head
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def reverseList(head):
    return _reverse(None, head)


def _reverse(prev, cur):
    if cur:
        next_node = cur.next
        cur.next = prev
        return _reverse(cur, next_node)
    else:
        return prev

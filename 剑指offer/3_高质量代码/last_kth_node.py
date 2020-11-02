"""
面试题15 链表中倒数第k个结点

要求：求单链表中的倒数第k个结点

思路：使用快慢指针，快的先走k-1步，需要考虑空链表以及k为0

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def last_kth(head, k):
    if not head or k <= 0:
        return None
    cur = head
    while cur and k - 1 >= 0:
        cur = cur.next
        k -= 1
    while cur:
        cur = cur.next
        head = head.next
    if k == 0:
        return head.val
    return None

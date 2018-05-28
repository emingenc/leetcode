# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Given a linked list, swap every two adjacent nodes and return its head.

# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
#
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Fork from https://github.com/kamyu104/LeetCode/blob/master/Python/swap-nodes-in-pairs.py
class Solution(object):
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    print(Solution().swapPairs(head))
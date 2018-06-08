"""
Leetcode 148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.

https://aaronice.gitbooks.io/lintcode/content/linked_list/sort_list.html
https://leetcode.com/problems/sort-list/description/


Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

"""
1. 找到链表中点：可以通过快慢指针的方法
2. 合并两个有序链表：链表的基本问题
3. 分治递归
"""

# Fork from https://github.com/kamyu104/LeetCode/blob/master/Python/sort-list.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None

        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)

        return self.mergeTwoLists(sorted_l1, sorted_l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)

        cur = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.next
            else:
                cur.next, cur, l2 = l2, l2, l2.next

        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2

        return dummy.next


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next= ListNode(2)
    print(Solution().sortList(head))

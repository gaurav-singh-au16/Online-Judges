"""
206. Reverse Linked List
Easy

5974

116

Add to List

Share
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

Accepted
1,225,464
Submissions
1,896,125
"""

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def reverseList(self, head: ListNode) -> ListNode:
            per = None
            cur = head
            while cur !=None:
                nxt = cur.next
                cur.next = per
                per = cur
                cur = nxt
            return per

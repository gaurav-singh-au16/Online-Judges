"""
21. Merge Two Sorted Lists
Easy

5798

699

Add to List

Share
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
Accepted
1,257,137
Submissions
2,264,946
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        
        p3 = None
        cur = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                if p3 is None:
                    p3 = ListNode(p1.val)
                    cur = p3
                else:
                    cur.next = ListNode(p1.val)
                    cur = cur.next
                p1 = p1.next
            else:
                if p3 is None:
                    p3 = ListNode(p2.val)
                    cur = p3
                else:
                    cur.next = ListNode(p2.val)
                    cur = cur.next
                p2 = p2.next    
        while p1 != None:
            cur.next = ListNode(p1.val)
            cur = cur.next
            p1 = p1.next
        while p2 != None:
            cur.next = ListNode(p2.val)
            cur = cur.next
            p2 = p2.next
        
            
        return p3
            
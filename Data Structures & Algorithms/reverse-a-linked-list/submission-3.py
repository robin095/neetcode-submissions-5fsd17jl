# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head
        else: 
            stored = self.reverseList(head.next)
            head.next = None
            curr = stored
            while curr.next:
                curr = curr.next
            curr.next = head
            return stored
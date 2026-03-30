# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2: 
            return list1

        curr1= list1
        curr2 = list2
        if list1.val <= list2.val:
            newest = list1
            head = list1
            curr1 = list1.next
        else:
            newest = list2
            head = list2
            curr2 = list2.next
        while(curr1 and curr2): 
            if curr1.val <= curr2.val:
                newest.next = curr1
                newest = curr1
                curr1 = curr1.next
            else:
                newest.next = curr2
                newest = curr2
                curr2 = curr2.next
        if curr1:
            newest.next = curr1
        else: 
            newest.next = curr2
        return head

        
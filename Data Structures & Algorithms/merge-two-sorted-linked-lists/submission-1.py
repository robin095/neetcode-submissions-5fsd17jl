# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_curr = list1
        list2_curr = list2

        result = ListNode(val=0, next=None)
        result_curr = result

        while (list1_curr != None) or (list2_curr != None):
            if list1_curr == None:
                result_curr.next = list2_curr
                return result.next
            elif list2_curr == None:
                result_curr.next = list1_curr
                return result.next
            elif (list1_curr.val < list2_curr.val):
                result_curr.next = list1_curr
                list1_curr = list1_curr.next
                result_curr = result_curr.next
            else:
                result_curr.next = list2_curr
                list2_curr = list2_curr.next
                result_curr = result_curr.next
        
        return result.next

        
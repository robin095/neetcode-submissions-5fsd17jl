# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        curr = head

        while curr:
            if curr.val in seen:
                if curr in seen[curr.val]:
                    return True
                else: seen[curr.val].append(curr)
            else: seen[curr.val] = [curr]
            curr = curr.next
        return False
        
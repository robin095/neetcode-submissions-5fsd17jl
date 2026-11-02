# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return (None)
        
        def mergeSort(lists, s, e):
            m = (s + e) // 2
            if s == e:
                return lists[s]
            first_list = mergeSort(lists, s, m)
            second_list = mergeSort(lists, m+1, e)
            return merge(first_list, second_list)
            
        
        def merge(first_list, second_list):
            result = ListNode()
            curr_result = result
            L = first_list
            R = second_list
            
            while L and R:
                if L.val < R.val:
                    curr_result.next = L
                    curr_result = curr_result.next
                    L = L.next
                else:
                    curr_result.next = R
                    curr_result = curr_result.next
                    R = R.next

            while L:
                curr_result.next = L
                curr_result = curr_result.next
                L = L.next
            
            while R:
                curr_result.next = R
                curr_result = curr_result.next
                R = R.next
            
            return result.next
        
        s = 0
        e = len(lists) - 1
        return mergeSort(lists, s, e)
            


        
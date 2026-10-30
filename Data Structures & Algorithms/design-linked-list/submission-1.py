class ListNode:
    def __init__(self, val=None, next= None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        if index < 0:
            return(-1)
        while curr:
            if index == i-1:
                return curr.val
            i += 1
            curr = curr.next
        return (-1)
            

    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = ListNode(val, temp)
        
        

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head 
        i = -1  
        while curr:
            if index < 0:
                temp = self.head.next
                self.head.next = ListNode(val, temp)
            elif i + 1 == index:
                temp = curr.next
                curr.next = ListNode(val, temp)
                return
            curr = curr.next
            i += 1

        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i = -1
        while curr:
            if i + 1 == index:
                if curr.next is None:
                    return
                else:
                    curr.next = curr.next.next
                    return
            curr = curr.next
            i += 1
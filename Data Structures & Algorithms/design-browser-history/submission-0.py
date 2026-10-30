class ListNode:
    
    def __init__(self, url=None, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url)
        self.cur.next.prev = self.cur
        self.cur = self.cur.next

        
    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.prev:
                self.cur = self.cur.prev
        return self.cur.url
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.next:
                self.cur = self.cur.next
        return self.cur.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
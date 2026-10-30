class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        new_q = deque()
        for i in range(len(self.q)-1):
            result = self.q.popleft()
            new_q.append(result)
        result = self.q
        self.q = new_q
        return result[0]

    def top(self) -> int:
        new_q = deque()
        for i in range(len(self.q)):
            result = self.q.popleft()
            new_q.append(result)
        self.q = new_q
        return result
        

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum and val < self.minimum[-1]:
            self.minimum.append(val)
        elif self.minimum: 
            self.minimum.append(self.minimum[-1])
        else: self.minimum.append(val)

        

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minimum = self.minimum[:-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        

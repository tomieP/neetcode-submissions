class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0: 
            self.minstack.append(val)
            return None
        if self.minstack and self.minstack[-1] >= val: 
            self.minstack.append(val)
            return None
        return None       

    def pop(self) -> None:
        if self.stack and self.minstack:
            if self.stack[-1] == self.minstack[-1]:
                temp = self.stack[-1]
                self.stack.pop()
                self.minstack.pop()
                return temp
            elif self.stack[-1] != self.minstack[-1]:
                temp = self.stack[-1]
                self.stack.pop()
                return temp
        else: return None      

    def top(self) -> int:
        if self.stack: return self.stack[-1]
        return 0    

    def getMin(self) -> int:
        if self.minstack: return self.minstack[-1]
        return 0
        

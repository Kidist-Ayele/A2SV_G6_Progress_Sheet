class MinStack:

    def __init__(self):
        self.stack = []
        self.my_dict = {}
        self.my_dict[0] = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        idx = len(self.stack)
        if idx == 1:
            self.my_dict[0] = val
        min_val = min(self.my_dict[idx - 1], val)
        self.my_dict[idx] = min_val
        

    def pop(self) -> None:
        idx = len(self.stack)
        del self.my_dict[idx]
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        idx = len(self.stack)
        return self.my_dict[idx]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
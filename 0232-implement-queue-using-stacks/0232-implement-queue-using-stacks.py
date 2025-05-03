class MyQueue:

    def __init__(self):
        self.queue_stack = deque()
        

    def push(self, x: int) -> None:
        self.queue_stack.append(x)
        

    def pop(self) -> int:
        return self.queue_stack.popleft()
        

    def peek(self) -> int:
        return self.queue_stack[0]
        

    def empty(self) -> bool:
        return not self.queue_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        return new_node

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = LinkedList()
        self.current = self.browser.append(homepage)
        

    def visit(self, url: str) -> None:
        new_node = self.browser.append(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1

        return self.current.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
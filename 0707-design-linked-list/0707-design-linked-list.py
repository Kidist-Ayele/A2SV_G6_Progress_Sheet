class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):

        self.dummy = Node()
        self.size = 0

        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: 
            return -1

        count = 0
        current = self.dummy.next
        while current:
            if index == count:
                return current.val
            current = current.next
            count += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        new_node = Node(val)
        count = 0

        current = self.dummy
        while current:
            if count == index:
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return
            current = current.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        count = 0

        current = self.dummy
        while current and current.next:
            if count == index:
                current.next = current.next.next
                self.size -= 1  
                return
            current = current.next
            count += 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

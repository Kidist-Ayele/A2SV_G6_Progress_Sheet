class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,key):
        """Appends a new node with the given key to the end of the list (most recently used)."""
        new_node = Node(key)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        return new_node

    def delete(self, node):
        """Removes the given node from the linked list."""

        if not node:
            return
        # If node is the head, move head forward
        if self.head == node:
            self.head = node.next
            if self.head:
                self.head.prev = None

        # If node is the tail, move tail backward
        if self.tail == node:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        
        # If node is in the middle
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        node.next = node.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.recency = LinkedList()
        self.node_store = defaultdict(tuple) # {key: (value, node)}

    def updateRecency(self, key):
        """Moves the given key to the most recently used position."""

        if key in self.node_store:
            old_node = self.node_store[key][1]    
            self.recency.delete(old_node)

        new_node = self.recency.append(key)
        return new_node

    def removeLRU(self):
        """Removes the least recently used key from the cache."""
        if not self.recency.head:
            return 

        lru_node = self.recency.head # Head is the least recently used
        self.recency.delete(lru_node)
        del self.node_store[lru_node.key]
        self.size -= 1

    def get(self, key: int) -> int:
        """Gets the value of the key if present in the cache, otherwise returns -1."""

        if key in self.node_store:
            value, _ = self.node_store[key]
            new_node = self.updateRecency(key)
            self.node_store[key] = (value, new_node)
            return value
        
        return -1

    def put(self, key: int, value: int) -> None:
        """Inserts a new key-value pair into the cache. If full, removes LRU entry first."""
        if key in self.node_store:
            new_node = self.updateRecency(key)
            self.node_store[key] = (value, new_node)
            return

        if self.size >= self.capacity:
            self.removeLRU()

        new_node = self.updateRecency(key)
        self.node_store[key] = (value, new_node)
        self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
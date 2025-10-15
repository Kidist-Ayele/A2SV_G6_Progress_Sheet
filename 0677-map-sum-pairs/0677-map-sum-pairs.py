class TrieNode:
    def __init__(self):
        self.is_end = False
        self.count = 0
        self.children = [None for _ in range(26)]

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        diff = val
        if key in self.map:
            diff -= self.map[key]
        self.map[key] = val

        cur = self.root
        for char in key:
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
            cur.count += diff
        cur.is_end = True
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                return 0
            cur = cur.children[idx]
        return cur.count

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

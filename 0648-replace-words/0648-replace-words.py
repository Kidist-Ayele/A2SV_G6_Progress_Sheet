class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class Solution:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def find_root(self, word):
        cur = self.root
        prefix = ""
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                return word
            cur = cur.children[idx]
            prefix += char
            if cur.is_end:
                return prefix
        return word


    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)

        words = sentence.split()
        ans = []
        
        for word in words:
            ans.append(self.find_root(word))
        
        return " ".join(ans)
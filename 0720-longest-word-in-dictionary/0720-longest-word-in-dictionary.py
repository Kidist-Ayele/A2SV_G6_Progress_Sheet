class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class Solution:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word):
        # if len(word) == 1:
        #     return True
        cur = self.root
        for i, char in enumerate(word):
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True
        return True

    def can_build(self, word):
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            cur = cur.children[idx]
            if not cur or not cur.is_end:
                return False
        return True
    
    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)

        words.sort()

        longest = ""
        for word in words:
            if self.can_build(word):
                if len(longest) < len(word):
                    longest = word
        return longest

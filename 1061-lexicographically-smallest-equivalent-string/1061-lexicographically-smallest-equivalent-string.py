class unionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if parent_x < parent_y:
                self.parent[parent_y] = parent_x
            else:
                self.parent[parent_x] = parent_y



class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = unionFind()
        letters = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(s1)):
            x = ord(s1[i]) - ord('a')
            y = ord(s2[i]) - ord('a')
            uf.union(x, y)
        ans = []
        for char in baseStr:
            index = ord(char) - ord('a')
            smallest_index = uf.find(index)
            ans.append(letters[smallest_index])
        
        return ''.join(ans)

        
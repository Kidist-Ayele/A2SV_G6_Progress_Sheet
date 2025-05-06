class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return
        if parent_x != parent_y:
            if self.size[parent_x] > self.size[parent_y]:
                self.size[parent_x] += self.size[parent_y]
                self.parent[parent_y] = parent_x
            else:
                self.size[parent_y] += self.size[parent_x]
                self.parent[parent_x] = parent_y
        self.count -= 1
        

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        return n - uf.count
        
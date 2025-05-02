class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.size[parent_x] > self.size[parent_y]:
                self.size[parent_x] += self.size[parent_y]
                self.parent[parent_y] = parent_x
            else:
                self.size[parent_y] += self.size[parent_x]
                self.parent[parent_x] = parent_y

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[0])):
                if isConnected[i][j] and uf.find(i) != uf.find(j):
                    uf.union(i, j)
                    n -= 1
        return n
        
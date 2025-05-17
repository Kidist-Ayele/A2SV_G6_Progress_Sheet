class unionFind:
    def __init__(self):
        self.parent = list(range(27))
        self.size = [1] * (27)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False

        if self.size[parent_x] > self.size[parent_y]:
            self.size[parent_x] += self.size[parent_y]
            self.parent[parent_y] = parent_x
        else:
            self.size[parent_y] += self.size[parent_x]
            self.parent[parent_x] = parent_y
        return True

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = unionFind()

        for q in equations:
            char1, char2 = ord(q[0]) - ord('a'), ord(q[-1]) - ord('a')
            if q[1] == '=':
                uf.union(char1, char2)

        for q in equations:
            char1, char2 = ord(q[0]) - ord('a'), ord(q[-1]) - ord('a')
            if q[1] == '!' and uf.find(char1) == uf.find(char2):
                return False


        return True
        
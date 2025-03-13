class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        
        if rowIndex == 0:
            return [1]

        prev = self.getRow(rowIndex - 1)
        cur = [1]

        for i in range(len(prev) - 1):
            cur.append(prev[i] + prev[i + 1])
        cur.append(1)
        
        return cur
        
            
        
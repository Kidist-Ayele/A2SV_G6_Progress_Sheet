class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        val = columnNumber

        res = ""
        while val > 0:
            added = (val - 1) % 26
            val = (val - 1) // 26
            res += chr(ord('A') + added)
        return res[::-1]

        
        
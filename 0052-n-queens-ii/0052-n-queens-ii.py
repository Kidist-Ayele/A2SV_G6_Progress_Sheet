class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        org_diagonal = set()
        rev_diagonal = set()

        ans = 0

        def backtrack(col):
            nonlocal ans
            if col == n:
                ans += 1
               
            
            for row in range(n):
                if (row in cols) or ((row + col) in org_diagonal) or ((col - row)  in rev_diagonal):
                    continue

                cols.add(row)
                org_diagonal.add(row + col)
                rev_diagonal.add(col - row)
                backtrack(col + 1)

                cols.remove(row)
                org_diagonal.remove(row + col)
                rev_diagonal.remove(col - row)

        backtrack(0)
        return ans


            
        
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiagonal = set()
        negDiagonal = set()
        ans = [["."]*n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in ans]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiagonal or (r - c) in negDiagonal:
                    continue

                cols.add(c)
                ans[r][c] = "Q"
                posDiagonal.add(r + c)
                negDiagonal.add(r - c)

                backtrack(r + 1)
                cols.remove(c)
                ans[r][c] = "."
                posDiagonal.remove(r + c)
                negDiagonal.remove(r - c)

        backtrack(0)
        return res




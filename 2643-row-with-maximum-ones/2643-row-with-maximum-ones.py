class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows = defaultdict(int)

        for i, row in enumerate(mat):
            rows[i] = row.count(1)

        max_val = max(list(rows.values()))

        for key, val in rows.items():
            if val == max_val:
                return [key, val]
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        queue = deque() 
        visit = set()
        res = [[-1] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    res[row][col] = 0
                    queue.append((row, col))
                    visit.add((row, col))
        
        while queue:
            row, col = queue.popleft()
            h = res[row][col]

            neighbors = [[row + 1, col], [row, col + 1], [row - 1, col], [row, col - 1]]

            for new_row, new_col in neighbors:
                if (new_col < 0
                    or new_row < 0 
                    or new_col == cols
                    or new_row == rows
                    or (new_row, new_col) in visit):

                    continue
                queue.append((new_row, new_col))
                visit.add((new_row, new_col))
                res[new_row][new_col] = h + 1
        return res




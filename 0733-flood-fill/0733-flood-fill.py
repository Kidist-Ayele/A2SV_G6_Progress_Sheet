class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]

        if old == color:
            return image

        directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}

        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))

        def dfs(row, col):

            if not inbound(row, col) or image[row][col] != old:
                return 

            image[row][col] = color
            
            for dx, dy in directions:
                new_row = dx + row
                new_col = dy + col

                dfs(new_row, new_col)
                
        dfs(sr, sc)

        return image
        
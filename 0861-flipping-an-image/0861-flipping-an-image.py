class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                if row[left] == 0 and row[right] == 0:
                    row[left] = 1
                    row[right] = 1
                elif row[left] == 1 and row[right] == 1:
                    row[left] = 0
                    row[right] = 0
                left += 1
                right -= 1
        return image

        
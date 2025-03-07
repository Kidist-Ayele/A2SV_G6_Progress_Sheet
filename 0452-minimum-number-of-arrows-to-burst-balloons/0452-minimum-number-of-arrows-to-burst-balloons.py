class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        result = len(points)
        left = points[0]
        
        for i in range(1, len(points)):
            current = points[i]

            if left[1] >= current[0]:
                result -= 1
                left = [current[0], min(current[1], left[1])]
            else:
                left = current
                
        return result

        
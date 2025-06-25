class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            point = x ** 2 + y ** 2
            distance.append([point, points[i]])
        
        distance.sort()
        res = []
        for i in range(k):
            res.append(distance[i][1])
        return res

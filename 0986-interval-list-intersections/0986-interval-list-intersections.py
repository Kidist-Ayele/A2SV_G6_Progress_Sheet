class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)

        point1 = point2 = 0
        ans = []

        while point1 < n and point2 < m:
            start1, end1 = firstList[point1]
            start2, end2 = secondList[point2]
            #If there is no intersection just move on
            if start1 > end2:
                point2 += 1
            elif start2 > end1:
                point1 += 1
            else:
                ans.append([max(start1, start2), min(end1, end2)])
                if end1 > end2:
                    point2 += 1
                else:
                    point1 += 1
        return ans



            
            

        
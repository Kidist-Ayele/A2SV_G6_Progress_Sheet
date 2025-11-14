class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        result = 0
        costs.sort(key=lambda x: x[1] - x[0])

        for i in range(n):
            if i < n//2:
                result += costs[i][1]
            else:
                result += costs[i][0]

        return result
        
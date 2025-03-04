class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        total = 0
        costs.sort(key=lambda x: abs(x[1] - x[0]), reverse = True)
        count_a = count_b = 0

        for cost_a, cost_b in costs:
            if cost_a <= cost_b: 
                if count_a < n//2:
                    total += cost_a
                    count_a += 1
                else:
                    total += cost_b
                    count_b += 1

            else:
                if count_b < n//2:
                    total += cost_b
                    count_b += 1
                else:
                    total += cost_a
                    count_a += 1

                
        return total

        
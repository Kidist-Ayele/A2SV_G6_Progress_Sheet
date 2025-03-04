class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        cur_gas = 0
        start = 0

        for right in range(len(gas)):
            cur_gas += gas[right] - cost[right]
            if cur_gas < 0:
                cur_gas = 0
                start = right + 1
        return start
        
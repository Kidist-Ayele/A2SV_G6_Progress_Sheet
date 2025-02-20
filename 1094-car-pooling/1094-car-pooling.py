class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * 1001

        for num, fro, to in trips:
            prefix[fro] += num
            if to < 1001:
                prefix[to] -= num

        cur_passenger = 0
        for i in range(1000):
            cur_passenger += prefix[i]
            if cur_passenger > capacity:
                return False
        
        return True
         

        
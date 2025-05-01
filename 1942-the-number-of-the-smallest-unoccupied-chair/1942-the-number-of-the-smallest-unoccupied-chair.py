class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrival_order = sorted((start, end, i) for i, (start, end) in enumerate(times))
        unoccupied = list(range(len(times) + 1))
        heapify(unoccupied)

        used_chairs = []

        for start, end, i in arrival_order:
             
            while used_chairs and start >= used_chairs[0][0]:
                leave_time, chair = heappop(used_chairs)
                heappush(unoccupied, chair)

            chair = heappop(unoccupied)
            heappush(used_chairs, (end, chair))

            if i == targetFriend:
                return chair

          
            
        
        
        
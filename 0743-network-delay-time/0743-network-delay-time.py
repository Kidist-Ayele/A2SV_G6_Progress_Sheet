class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for edge in times:
            u, v, w = edge
            graph[u].append((v, w))

        min_heap = []
        heappush(min_heap, (0, k))
        shortest_time = {}

        min_len = 0

        while min_heap:
            time, node = heappop(min_heap)
            if node in shortest_time:
                continue

            shortest_time[node] = time
            cur_len = 0

            for child, weight in graph[node]:
                if child not in shortest_time:
                    heappush(min_heap, (time + weight, child))
       
        if len(shortest_time) == n:
            return max(shortest_time.values())
        return -1
        
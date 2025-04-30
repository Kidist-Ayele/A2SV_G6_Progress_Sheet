class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for edge in times:
            u, v, t = edge
            graph[u].append((v, t))
        
        queue = deque([k])
        visited = set()

        min_len = 0

        while queue:
            node = queue.popleft()
            visited.add(node)
            cur_len = 0

            for child in graph[node]:
                if child not in visited:
                    queue.append(child[0])
                    cur_len = max(cur_len, child[1])

            min_len += cur_len
        # print(visited)
        if len(visited) != n:
            return -1
        return min_len
        
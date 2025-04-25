class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * (len(quiet))

        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque()

        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        
        ancestors = [set() for _ in range(len(quiet))]

        while queue:
            node = queue.popleft()

            for child in graph[node]:
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        ans = []
        for x in range(len(quiet)):
            cur_min = quiet[x]
            cur_val = x
            for y in ancestors[x]:
                if quiet[y] < cur_min:
                    cur_min = quiet[y]
                    cur_val = y
            ans.append(cur_val)
        
        return ans


        
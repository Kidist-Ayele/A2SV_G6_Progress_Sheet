class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        ancestors = [set() for _ in range(numCourses)]

        while queue:
            node = queue.popleft()

            for child in graph[node]:
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        result = []

        for u, v in queries:
            if u in ancestors[v]:
                result.append(True)
            else:
                result.append(False)

        return result


        
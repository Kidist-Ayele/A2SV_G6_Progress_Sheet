class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        order = []

        queue = deque()

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        for node, degree in enumerate(indegree):
            if degree == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()

            for child in graph[node]:
                indegree[child] -= 1

                if indegree[child] == 0:
                    queue.append(child)

            order.append(node)
        if len(order) != numCourses:
            return []
        return order




        
        
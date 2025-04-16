class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)

        for u, v in redEdges:
            redGraph[u].append(v)

        for u, v in blueEdges:
            blueGraph[u].append(v)
        
        queue = deque()
        queue.append((0, 'red'))
        queue.append((0, 'blue'))

        count = 0

        ans = [-1] * n
        ans[0] = 0

        visited = set()
        visited.add((0, 'red'))
        visited.add((0, 'blue'))

        while queue:
            
            level = len(queue)

            for _ in range(level):
                node, color = queue.popleft()

                # Alternate
                if color == 'red':
                    for child in blueGraph[node]:
                        if (child, 'blue') not in visited:
                            visited.add((child, 'blue'))
                            queue.append((child, 'blue'))
                            if ans[child] == -1:
                                ans[child] = count + 1

                else:
                    for child in redGraph[node]:
                        if (child, 'red') not in visited:
                            visited.add((child, 'red'))
                            queue.append((child, 'red'))
                            if ans[child] == -1:
                                ans[child] = count + 1
                
            count += 1

        return ans


        
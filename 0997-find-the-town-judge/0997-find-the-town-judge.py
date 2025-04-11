class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        trusted = defaultdict(int)

        for row in trust:
            u, v = row
            graph[u].append(v)
            trusted[v] += 1

        for i in range(1, n + 1):
            if not graph[i] and trusted[i] == n - 1:
                return i
        return -1



        
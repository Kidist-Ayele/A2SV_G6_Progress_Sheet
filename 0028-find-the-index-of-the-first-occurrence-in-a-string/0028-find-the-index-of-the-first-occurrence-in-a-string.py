class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Using Queue
        if len(haystack) < len(needle):
            return -1

        n, m = len(haystack), len(needle)

        queue = deque()
        for i in range(n):
            queue.append(haystack[i])

            if len(queue) > m:
                queue.popleft()

            if ''.join(queue) == needle:
                return (i - m + 1)

        return -1
        
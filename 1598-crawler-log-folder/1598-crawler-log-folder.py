class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for folder in logs:
            if folder == './':
                continue
            if folder == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        return len(stack)
        
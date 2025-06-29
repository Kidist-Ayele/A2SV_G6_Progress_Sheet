class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        Stack = []
        for d in num:
            while Stack and k > 0 and Stack[-1] > d:
                Stack.pop()
                k -= 1
            Stack.append(d)
        Stack = Stack[:-k] if k else Stack
        res = ''.join(Stack).lstrip('0')
        return res if res else '0'
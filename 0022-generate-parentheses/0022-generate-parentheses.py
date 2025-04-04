class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(num_open, num_close):
            if num_open == num_close == n:
                ans.append("".join(stack))
                return
            
            if num_open < n:
                stack.append('(')
                backtrack(num_open + 1, num_close)
                stack.pop()
            
            if num_open > num_close:
                stack.append(')')
                backtrack(num_open, num_close + 1)
                stack.pop()

        backtrack(0, 0)
        return ans
        
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1]
        ans = 0
        for i, num in enumerate(arr):
            while stack[-1] != -1 and arr[stack[-1]] > num:
                index = stack.pop()
                ans += (index - stack[-1]) * (i - index) * arr[index]
            stack.append(i)

        while stack[-1] != -1:
            index = stack.pop()
            ans += (index - stack[-1]) * (len(arr) - index) * arr[index]

        return ans %(10**9 + 7)


        

        
        
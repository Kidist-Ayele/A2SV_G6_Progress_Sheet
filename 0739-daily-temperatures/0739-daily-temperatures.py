class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i, num in enumerate(temperatures):
            
            while stack and num > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
                
   
            
            stack.append(i)
            
        return ans
        
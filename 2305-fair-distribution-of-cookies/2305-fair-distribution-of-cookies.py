class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs = [0] * k
        ans = float("inf")

        def backtrack(index):
            nonlocal ans
            if index >= len(cookies):
                ans = min(ans, max(childs))
                return 

            for i in range(k):
                childs[i] += cookies[index]
                backtrack(index + 1)

                childs[i] -= cookies[index]
            
        
        backtrack(0)
        return ans
        
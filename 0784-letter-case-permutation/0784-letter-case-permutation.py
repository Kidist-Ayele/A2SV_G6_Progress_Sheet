class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        
        def helper(i, curr):
            if i == n:
                ans.append(''.join(curr))
                return
            if s[i].isalpha():
                helper(i+1, curr + [s[i].swapcase()])
            helper(i+1, curr + [s[i]])
                
        helper(0, [])
        return ans
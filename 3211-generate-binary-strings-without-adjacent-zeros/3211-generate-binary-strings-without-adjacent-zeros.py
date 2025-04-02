class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        path = []

        def backtrack(index):
            if index == n:
                ans.append(''.join(path))
                return
            
            # choose '1'
            path.append('1')
            backtrack(index + 1)
            path.pop()

            #choose '0'
            if not path or path[-1] != '0':
                path.append('0')
                backtrack(index + 1)
                path.pop()


        backtrack(0)
        return ans
            

        
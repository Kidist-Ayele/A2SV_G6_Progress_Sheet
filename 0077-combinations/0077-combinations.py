class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = [x for x in range(1, n + 1)]
        # print(candidates)
        ans = []
        def backtrack(index, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            
            if index == n:
                return

            # Take
            path.append(candidates[index])
            backtrack(index + 1, path)

            # Not take
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])
        return ans

            

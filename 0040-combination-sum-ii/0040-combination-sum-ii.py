class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def backtrack(index, total):
            if total == target:
                ans.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if total > target:
                    break
                    
                path.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                path.pop()
            
        backtrack(0, 0)
        return ans

        
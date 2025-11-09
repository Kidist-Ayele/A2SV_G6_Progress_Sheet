class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0  
        
        mod_index = {0: -1}  
        cur = 0
        best = n  
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            target = (cur - need) % p
            if target in mod_index:
                length = i - mod_index[target]
                if length < best:
                    best = length
        
            mod_index[cur] = i
        
        return best if best < n else -1

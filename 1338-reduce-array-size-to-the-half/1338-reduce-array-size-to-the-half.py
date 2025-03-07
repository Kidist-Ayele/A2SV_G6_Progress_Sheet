class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = Counter(arr)
        res = 0
        target = 0
        sort_count = sorted(count.values(), reverse= True)
        for val in sort_count:
            target += val
            res += 1
            if target >= n//2:
                return res
        
        

        
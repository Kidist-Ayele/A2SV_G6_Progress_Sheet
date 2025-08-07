class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        arr1.sort()
        arr2_set = set(arr2)
        res = []
        for num in arr2:
            res.extend([num]*count[num])
        for x in arr1:
            if x not in arr2_set:
                res.append(x)
        return res

        
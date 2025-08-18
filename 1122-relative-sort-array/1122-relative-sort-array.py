class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        num_set = set(arr2)
        result = []
        for num in arr2:
            temp = [num] * count[num]
            result.extend(temp)
        remain = []
        for num in arr1:
            if num not in num_set:
                remain.append(num)
                
        remain.sort()
        result.extend(remain)
        return result

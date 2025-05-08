class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_arr = []
        cur_max = -1

        for i in range(len(arr) - 1, -1, -1):
            max_arr.append(cur_max)
            cur_max = max(cur_max, arr[i])
        return max_arr[::-1]

        
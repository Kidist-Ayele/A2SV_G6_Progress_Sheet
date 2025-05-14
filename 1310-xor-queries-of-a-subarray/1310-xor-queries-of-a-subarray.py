class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        ans = []

        cur_xor = 0
        for num in arr:
            cur_xor ^= num
            pref.append(cur_xor)
            
        for left, right in queries:
            ans.append(pref[right + 1] ^ pref[left])
        return ans


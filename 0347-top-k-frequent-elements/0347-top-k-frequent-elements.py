class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        count = Counter(nums)

        for val, freq in count.items():
            heappush(heap, (-freq, val))
        
        for i in range(k):
            _, val = heappop(heap)
            ans.append(val)
        return ans


        
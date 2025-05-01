class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []

        for word, freq in count.items():
            heappush(heap, (-freq, word))
        
        res = []
        for _ in range(k):
            freq, word = heappop(heap)
            res.append(word)
            
        return res


        
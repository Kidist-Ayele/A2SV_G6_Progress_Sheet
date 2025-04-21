class Solution:
    def sortSentence(self, s: str) -> str:
        order = defaultdict(str)  
        words = s.split()  
        
        for word in words:  
            n = len(word)
            order[int(word[-1])] = word[:n - 1]  # Store word without the number
        
        ans = []
        for key in sorted(order.keys()):  
            ans.append(order[key])
        
        return " ".join(ans) 

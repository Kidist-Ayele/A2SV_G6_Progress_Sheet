class Solution:
    def printVertically(self, s: str) -> List[str]:
        # Collect words from the string
        words = s.split()
        max_len = 0
        result = []

        # Find maximum size from words
        for word in words:
            max_len = max(max_len, len(word))
        
        # Iterate through them and collect same indexed letters 
        for i in range(max_len):
            ans = ""
            right = 0
            while right < len(words):
                if i >= len(words[right]):
                    ans += " "
                else:
                    ans += words[right][i]
                right += 1
            
            # Remove space from the end of string and add it to result array
            result.append(ans.rstrip())
        return result



        
class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        keyboard ={1:"qwertyuiop", 2:"asdfghjkl", 3:"zxcvbnm"}
        result = []

        for word in words:
            row_set = set()

            for char in word:
                if char.lower() in keyboard[1]:
                    row_set.add(1)
                elif char.lower() in keyboard[2]:
                    row_set.add(2)
                elif char.lower() in keyboard[3]:
                    row_set.add(3)
                    
            if len(row_set) == 1:
                result.append(word)
        return result





        
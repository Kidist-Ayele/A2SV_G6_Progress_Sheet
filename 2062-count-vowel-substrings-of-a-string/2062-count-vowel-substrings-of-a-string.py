class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'u':1, 'a':1, 'e':1, 'i':1, 'o':1}
        count = 0
        n = len(word)

        for i in range(n):
            seen = set()

            for j in range(i, n):
                if word[j] in vowels:
                    seen.add(word[j])
                    if len(seen) == 5:
                        count += 1
                else:
                    break
                    
        return count

        
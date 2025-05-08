class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []

        for char in set(words[0]):
            count = min(word.count(char) for word in words)
            ans.extend([char] * count)
        return ans
        
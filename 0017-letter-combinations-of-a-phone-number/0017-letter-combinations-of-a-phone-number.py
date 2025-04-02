class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        chars = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = []
        path = []

        def backtrack(index):
            if index == len(digits):
                ans.append("".join(path))
                return

            digit = int(digits[index]) - 2
            for letter in chars[digit]:
                path.append(letter)
                backtrack(index + 1)
                path.pop()


        backtrack(0)
        return ans
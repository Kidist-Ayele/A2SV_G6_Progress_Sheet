class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        if not wordDict:
            return False

        word_len = sorted({len(x) for x in wordDict})
        word_list = set(wordDict)
        @cache
        def dp(idx):
            if idx == len(s):
                return True

            for L in word_len:
                j = idx + L

                if j > len(s):
                    break
                if s[idx:j] in word_list and dp(j):
                    return True
            return False

        return dp(0)

            

            
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0

        for right, char in enumerate(s):
            count[char] += 1

            while len(count) < right - left + 1:
                count[s[left]] -= 1

                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans = max(ans, right - left + 1)

        return ans
        
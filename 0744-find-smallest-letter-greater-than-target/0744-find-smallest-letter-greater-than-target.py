class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        ans = ""
        while left <= right:
            print(left, right)
            mid = (right + left) // 2
            # print(letters[mid] >= target)
            if letters[mid] <= target:
                left = mid + 1
            else:
                ans = letters[mid]
                # print(ans)
                right = mid - 1
        if ans == "":
            return letters[0]
        return ans
        
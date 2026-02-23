class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        ans = []
        # Binary Search X
        def binary_search(x):
            left, right = 0, n - 1
            ans = -1
            while left <= right:
                mid = (right + left) // 2
                if arr[mid] <= x:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        idx = binary_search(x)
        left = idx
        right = idx + 1

        # pick k closest elements
        while len(ans) < k:
            if left >= 0 and right < n:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            elif left >= 0:
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1

        ans.sort()
        return ans

        
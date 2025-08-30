class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            l_most = max(mid-1,l)
            r_most = min(mid + 1, r)

            if nums[l] <= nums[l_most]:
                if target >= nums[l] and target <= nums[l_most]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[r_most] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return -1

        
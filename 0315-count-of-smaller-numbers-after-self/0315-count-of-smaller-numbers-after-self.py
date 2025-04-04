class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        We will store the original indices and count the smaller elements for each index.  
        This means counting how many right-side elements are merged before each number during 
        merge sort.  
        We use a modified merge sort to efficiently track these counts while sorting.

        '''
        index = [0] * len(nums)
        indices = list(range(len(nums)))

        def merge(left_half, right_half):
            left = right = 0
            ans = []

            while left < len(left_half) and right < len(right_half):
                if nums[left_half[left]] <= nums[right_half[right]]:
                    ans.append(left_half[left])
                    index[left_half[left]] += right
                    left += 1
                else:
                    ans.append(right_half[right])
                    right += 1

            while left < len(left_half):
                index[left_half[left]] += right
                ans.append(left_half[left])
                left += 1

            while right < len(right_half):
                ans.append(right_half[right])
                right += 1
            return ans
        
        def merge_sort(left, right):
            if left == right:
                return [indices[left]]
            mid = left + (right - left) // 2

            left_half = merge_sort(left, mid)
            right_half = merge_sort(mid + 1, right)

            return merge(left_half, right_half)

        merge_sort(0, len(nums) - 1)
        return index


        
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        index = defaultdict(int)
        for i, num in enumerate(nums2):
            index[num] = i

        ans = [-1] * len(nums2)
        for i, num in enumerate(reversed(nums2)):
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                ans[i] = stack[-1]

            stack.append(num)
        ans.reverse()

        result = []
        for num in nums1:
            result.append(ans[index[num]])

        return result
        


        